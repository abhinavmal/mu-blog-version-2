from Handler import Handler
from Decorators import post_exists
from models import *
import time

class EditPost(Handler):
    @post_exists
    def get(self, post_id, post):
        user = self.check_user_cookie("user_id")
        if not user:
            self.redirect("/login")
            return
        self.render("edit_post.html", user=user, title=post.title,
                    body=post.body, post_id=str(post_id))

    @post_exists
    def post(self, post_id, post):
        title = self.request.get("subject").strip()
        body = self.request.get("content").strip()
        user = self.check_user_cookie("user_id")
        if not user:
            self.redirect("/login")
            return
        if title and body:
            post.title = title
            post.body = body
            p_key = post.put()
            # Time.sleep() for eventual consistency of the database
            time.sleep(0.1)
            self.redirect("/singlepost/"+str(p_key.id()))
            return
        else:
            error = "We need both a title and some body!"
            self.render("edit_post.html", error=error, title=title,
                        body=body, user=user)
