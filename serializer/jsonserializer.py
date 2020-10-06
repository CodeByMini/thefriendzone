from json import JSONEncoder

class Encoder(JSONEncoder):
    def default(self, user):
        return user.__dict__