from framework.resources.albums import Albums
from framework.resources.comments import Comments
from framework.resources.photos import Photos
from framework.resources.posts import Posts
from framework.resources.todos import Todos
from framework.resources.users import Users


class Client:

    @property
    def albums(self):
        return Albums()

    @property
    def posts(self):
        return Posts()

    @property
    def comments(self):
        return Comments()

    @property
    def photos(self):
        return Photos()

    @property
    def todos(self):
        return Todos()

    @property
    def users(self):
        return Users()
