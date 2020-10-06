from dao.userdao import UserDao
from dao.postdao import PostDao
from models.user import User

class Engine:
    """
    Engine object. 
    Provides the Social network app a main
    interface, to organize and keep track
    of users and post relations.
    """
    def __init__(self):
        self._active_user = None
        self._user_dao = UserDao(filepath="users.json")
        self._post_dao = PostDao(filepath="posts.json")

    def add_user(self, username, password):
        """
        Adds a user to the user dao object.
        :param username:
            str, username for the user
        :param password:
            str, password for the user
        """
        new_user = User(username, password)
        self._user_dao.add(key=new_user.username, value=new_user)

    def add_post(self, user, body):
        new_post = Post(author=user, body=body)
        
        list_of_posts = self._post_dao.get(user)
        if list_of_posts is None:
            self._post_dao.add(user, [])        
        list_of_posts.append(new_post)

    def log_in(self, username, password):
        user = self._user_dao.get(username)
        if user is None or password != user.password:
            raise RuntimeError("Password or username incorrect")

        user.update_last_seen()
        self._active_user = username
        self._user_dao.save_to_file()

        return user