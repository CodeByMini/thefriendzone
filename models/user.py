from models.status import Status
from datetime import datetime

class User:
    """
    The User object represents a person, 
    bot or entity registered as a user
    in the application. 

    username:
        (str)
    password:
        (str)
    last_seen:
        (str)
        timestamp when the user was latest
        recorded as active. Mutates with update_last_seen().
    buddies:
        (dict <str, User>)
    status:
        (Status enum)
    """
    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._last_seen = None
        self._buddies = dict()
        self._status = Status.offline

    def __repr__(self):
        return f"User(username: {self._username}"

    def __str__(self):
        return f"{self._username}, last seen: {self._last_seen}"

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, val):
        self._username = val

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, val):
        self._password = val

    @property
    def buddies(self):
        return self._buddies

    @property
    def last_seen(self):
        return self._last_seen

    def update_last_seen(self):
        self._last_seen = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    def add_buddy(self, buddy):
        self._buddies['buddies'] = buddy

    def remove_buddy(self, username) -> bool:
        try:
            del self._buddies[username]
        except KeyError:
            return False
        return True