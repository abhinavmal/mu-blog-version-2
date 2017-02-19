from Handler import *
from models.User import *


class LoginHandler(Handler):
    def get(self):
        self.render("login.html", username_error="", password_error="")

    def post(self):
        # Strip trailing spaces, if they exist
        username = self.request.get("username").strip()
        password = self.request.get("password")
        username_error = ""
        password_error = ""
        if not valid_username(username):
            username_error = "That is not valid username"
        if not valid_password(password):
            password_error = "That is not valid password"
        if username_error or password_error:
            self.render("login.html", username_error=username_error,
                        password_error=password_error, username=username)
        else:
            # check for valid username in database
            u = User.return_valid_user_obj(username, password)
            if u:
                self.login(u)
                self.redirect("./registered")
                return
            username_error = "Username/Password Invalid!"
            password_error = "Username/Password Invalid!"
            self.render("login.html", username_error=username_error,
                        password_error=password_error, username=username)
