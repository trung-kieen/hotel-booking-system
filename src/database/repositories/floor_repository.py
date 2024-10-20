from database.repositories.base_repository import Repository
from utils.singleton import singleton
from database.models.floor import Floor
@singleton
class FloorRepository(Repository[Floor]):
    def __init__(self):
        super().__init__()
    # pass
