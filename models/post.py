from datetime import datetime

class Post:
    def __init__(self, author, body)
        self._author = author
        self._body = body
        self._created_timestamp = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        self._yikes = 0
        self._attachments = []

    @property
    def yikes(self):
        return self._yikes

    @property
    def author(self):
        return self._author

    def yike(self):
        self._yikes += 1

    def un_yike(self):
        if self._yikes > 0:
            self._yikes -= 1

    def attach(self, attachment):
        self._attachments.append(attachment)