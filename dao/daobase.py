class DaoBase:
    """
    BaseClass for a Data Access Object
    """
    def __init__(self):
        self._lookup = {}

    @property
    def all(self) -> dict:
        """
        Get the entire structure
        :returns: dict
        """
        return self._lookup

    def add(self, key, value) -> None:
        """
        Add key value pair.
        :param key: Any
        :param value: Any
        :returns: None
        """
        if not key in self._lookup:
            self._lookup[key] = value

    def get(self, key):
        """
        Get value behind key
        :param key: Any
        :returns: Any
        """
        try:
            return self._lookup[key]
        except KeyError:
            return None