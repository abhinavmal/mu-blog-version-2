from Handler import Handler
from models import *


class LogoutHandler(Handler):
    def get(self):
        # Delete Cookie
        self.logout()
        self.redirect("./")
        return
