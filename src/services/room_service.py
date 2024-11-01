"""
Author: Nguyen Khac Trung Kien
Wraping detail how to work with data in service layer
"""
from collections.abc import Iterable

from database.engine import EngineHolder
from database.models import bed_room
from database.models.bed_room import BedRoom
from database.models.bed_type import BedType
from database.models.room import Room
from database.orm import Session
from database.repositories import bed_room_repository, room_repository
from database.repositories.bed_room_repository import BedRoomRepository
from database.repositories.bed_type_repository import BedTypeRepository
from database.repositories.room_repository import RoomRepository
from utils.decorator import handle_exception, transaction
from utils.singleton import singleton


@singleton
class RoomService:
    def __init__(self):
        self.room_repo = RoomRepository[Room]()
        self.bed_type_repo = BedTypeRepository[BedType]()
        self.bed_room_repo : BedRoomRepository[BedRoom]= BedRoomRepository[BedRoom]()

    # def get_detail_booking(self):
    #     pass


    def delete_room_by_id(self , room_id ):
        self.room_repo.delete_by_id(room_id)

    def get_room_by_id(self, room_id):
        return self.room_repo.get_by_id(room_id)
    def get_all_bed_types(self ):
        return self.bed_type_repo.get_all_bed_types()


    def get_bed_type_by_id(self , bed_type_id ):
        return self.bed_type_repo.get_bed_type_by_id(bed_type_id)
    def get_all_bed_by_room_id(self , room_id) -> Iterable[BedRoom]:
        """
        Return a list of bed_id filter by bed room
        """
        return  self.bed_room_repo.get_all_by_room_id(room_id)


    def delete_bed_room_by_room_id_and_bed_type(self , room_id , type_id ) -> None :
        self.bed_room_repo.delete_by_room_id_and_bed_type(room_id , type_id)


    @handle_exception
    @transaction
    def update_room_and_bed (self,  updated_room : Room , bed_rooms : Iterable[BedRoom], session  = None  ):
        session.merge(updated_room)
        # After persistence with merge updated_room will have information about room id

        bed_rooms_from_database = self.get_all_bed_by_room_id(updated_room.id)
        bed_type_ids_before = set([bed_room.bed_type_id for bed_room in  bed_rooms_from_database])

        # After is get from form dialog input field
        bed_type_ids_after = set([bed.bed_type_id  for bed in bed_rooms])

        added_bed_type_id = bed_type_ids_after - bed_type_ids_before
        updated_bed_type_id = bed_type_ids_after &  bed_type_ids_before
        deleted_bed_type_id =   bed_type_ids_before  -  bed_type_ids_after

        for type_id in deleted_bed_type_id:
            self.delete_bed_room_by_room_id_and_bed_type(updated_room.id  , type_id)
        for bed  in bed_rooms:
            if bed.bed_type_id in added_bed_type_id:
                session.merge(bed)
            elif bed.bed_type_id in updated_bed_type_id:
                session.merge(bed)

    def exist_booking_with_room(self, room_id):
        """
        Use to check if room have book/reservation by any customer
        """
        num_booking_relate= int(EngineHolder().scalar("SELECT COUNT(*) FROM bookings WHERE room_id = :room_id", room_id = room_id))
        if num_booking_relate > 0:
            return True
        return False

    @handle_exception
    @transaction
    def add_room_and_bed (self , new_room  : Room , bed_rooms : Iterable [ BedRoom], session= Session()):
        session.add(new_room)
        # Need to persistence room before to get new room id
        session.commit()

        for bed in bed_rooms:
            bed.room_id = new_room.id
            session.add(bed)





