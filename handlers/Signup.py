import time
from Handler import *
from models import *


class SignupHandler(Handler):
    def validate_input(self, username, password, verify_pass, email):
        username_error = ""
        password_error = ""
        password_error_start = ""
        email_error = ""
        have_error = False
        params = dict()
        if not password or not valid_password(password):
            params["password_error_start"] = "That password was not correct."
            have_error = True
        if password != verify_pass:
            params["password_error"] = "Your passwords didn't match."
            have_error = True
        if (' ' in username) or not username or \
           not valid_username(username):
            params["username_error"] = "Not valid username. Valid one is " + \
                                       "min 3 & max 20 chars, where chars " + \
                                       "can be letters, alphabets, '_' or '-'"
            have_error = True
        if email and ('@' not in email) and ('.' not in email) or \
           not valid_email(email):
            params["email_error"] = "That's not a valid email."
            have_error = True
        if have_error:
            return params
        else:
            return None

    def get(self):
        self.render("signup.html", username_error="", password_error_start="",
                    password_error="", email_error="")

    def post(self):
        username = self.request.get("username").strip()
        password = self.request.get("password")
        verify_pass = self.request.get("verify")
        email = self.request.get("email").strip()
        error_params = self.validate_input(username, password,
                                           verify_pass, email)
        #  Check is username exists
        username_exists_error = None
        existing_user = User.query(User.username == username).fetch(1)
        if existing_user:
            error_params["username_exists_error"] = "This username \
                                                     already exists."
        if username_exists_error or error_params:
            self.render("signup.html", **error_params)
        else:
            user_obj = User(username=username,
                            pw_hash=make_pw_hash(username, password),
                            email=str(email))
            user_key = user_obj.put()
            self.set_secure_cookie("user_id", str(user_key.id()))
            self.redirect("./registered")
            return
