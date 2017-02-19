from Handler import Handler
from Decorators import comment_exists
from models import *


class DeleteComment(Handler):
    @comment_exists
    def get(self, post_id, comment_id, post, comment):
        user = self.check_user_cookie("user_id")
        if not user:
            self.redirect("/login")
            return
        del_comment = Comment.get_by_id(long(comment_id))
        if del_comment:
            if user.key != del_comment.author:
                self.logout()
                return self.redirect("/login")
            del_title = post.title
            del_body = post.body
            del_likes = post.num_likes
            del_dislikes = post.num_dislikes
            del_author = post.author
            # Delete the specific comment associated with the post
            del_comment.key.delete()
            self.render("delete_comment.html", del_comment=del_comment,
                        user=user, title=post.title, body=post.body,
                        author=post.author, post_id=str(post_id))
        else:
            self.redirect("/")
            return
