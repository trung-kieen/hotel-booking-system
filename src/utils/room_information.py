"""
Author: Dang Xuan Lam
"""
from database.models.room import Room


def get_room_location(id, floor):
    return f" Room: {id % 10 if id < 10 else id % 10 + 1} Floor: {floor}"


def get_base_information(room: Room):
    return f"Room: {room.id} Type: {room.room_type} Floor: {room.floor_id} Price: {room.price} Bed: {" ".join([x.name for x in room.bed_types])}"
