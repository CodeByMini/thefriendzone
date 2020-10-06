from dao.daobase import DaoBase
from serializer.jsonserializer import Encoder
import json

class UserDao(DaoBase):
    def __init__(self, filepath):
        super().__init__()
        self._user_filepath = filepath

    def __repr__(self):
        return f"PostDao({self._lookup.keys()})"

    def save_to_file(self):
        with open(self._user_filepath, "w", encoding="utf-8") as f:
            f.write(json.dumps(self._lookup, cls=Encoder, indent=2))

    def read_from_file(self):
        with open(self._user_filepath, "r", encoding="utf-8") as f:
            data = f.read()
            self._lookup = json.loads(data)