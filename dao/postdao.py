from dao.daobase import DaoBase
import json

class PostDao(DaoBase):
    def __init__(self, filepath):
        super().__init__()
        self._user_filepath = filepath

    def __repr__(self):
        return f"PostDao({self._lookup.keys()})"

    def save_to_file(self):
        with open(self._user_filepath, "w", encoding="utf-8") as f:
            f.write(json.dumps(self._lookup))

    def read_from_file(self):
        with open(self._user_filepath, "r", encoding="utf-8") as f:
            data = f.read()
            self._lookup = json.loads(data)