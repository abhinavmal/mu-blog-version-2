from Handler import Handler
from Decorators import post_exists
from models import *

class DeletePost(Handler):
    @post_exists
    def get(self, post_id, post):
        user = self.check_user_cookie("user_id")
        if not user:
            self.redirect("/login")
            return
        if post:
            del_title = post.title
            del_body = post.body
            del_likes = post.num_likes
            del_dislikes = post.num_dislikes
            del_author = post.author
            del_date = post.get_date()
            del_time = post.get_time()
            # Delete all comments associated with the post
            comments = Comment.query(Comment.for_post == str(post_id))
            for comment in comments:
                comment.key.delete()
            post.key.delete()
            self.render("delete_post.html", user=user, title=del_title,
                        body=del_body, author=del_author,
                        post_id=str(post_id), date=del_date, time=del_time)
        else:
            self.redirect("/")
            return
