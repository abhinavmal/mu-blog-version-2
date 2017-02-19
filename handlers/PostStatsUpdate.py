import time

# JSON
import json

from Handler import Handler
from models import *


# Function to handle the AJAX request for liking or disliking a post
class PostStatsUpdate(Handler):
    def post(self):
        user = self.check_user_cookie("user_id")
        if not user:
            self.redirect("/login")
            return
        post_id = self.request.get("post_id")
        update_type = self.request.get("type")
        post = Post.get_by_id(long(post_id))
        if not post:
            self.redirect('/error')
            return
        if update_type == "like" and user.key in post.dislikes:
            data = {"error": "You already " +
                             "disliked this one! Can't like it now!"}
            self.response.out.write(json.dumps(data))
            return
        if update_type == "dislike" and user.key in post.likes:
            data = {"error": "You already " +
                             "liked this one! Can't dislike it now!"}
            self.response.out.write(json.dumps(data))
            return
        if update_type == "like" and user.key not in post.likes:
            post.likes.append(user.key)
            post.put()
            time.sleep(0.5)
            data = {"count": post.num_likes}
            self.response.out.write(json.dumps(data))
        elif update_type == "dislike" and user.key not in post.dislikes:
            post.dislikes.append(user.key)
            post.put()
            time.sleep(0.5)
            data = {"count": post.num_dislikes}
            self.response.out.write(json.dumps(data))
        else:
            data = {"error": "You already " + update_type +
                             "d this one!"}
            self.response.out.write(json.dumps(data))
        return
