from Handler import Handler
from models import *


class ErrorHandler(Handler):
    def get(self):
        user = self.check_user_cookie("user_id")
        if not user:
            self.redirect("/login")
            return
        self.render("error.html", user=user)
