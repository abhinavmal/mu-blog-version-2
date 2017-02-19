import time
from Handler import Handler
from models import *


class CreatePost(Handler):
    def get(self):
        user = self.check_user_cookie("user_id")
        if not user:
            self.redirect("/login")
            return
        else:
            self.render("create_post.html", user=user)

    def post(self):
        user = self.check_user_cookie("user_id")
        if not user:
            self.redirect("/login")
            return
        title = self.request.get("subject")
        body = self.request.get("content")
        if title and body:
            post = Post(title=title, body=body, author=user.key)
            post_key = post.put()
            # Time.sleep() for eventual consistency of the database
            time.sleep(0.1)
            self.redirect("/singlepost/"+str(post_key.id()))
            return
        else:
            error = "We need both a title and some body!"
            self.render("create_post.html", error=error, title=title,
                        body=body, user=user)
