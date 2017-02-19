from Handler import Handler
from models import *


class ValidPage(Handler):
    def get(self):
        user = self.check_user_cookie("user_id")
        if not user:
            self.redirect("/login")
            return
        self.render("registered.html", user=user)
