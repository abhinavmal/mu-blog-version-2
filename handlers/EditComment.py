from Handler import Handler
from models import *
import time


class EditComment(Handler):
    def get(self, post_id, comment_id):
        user = self.check_user_cookie("user_id")
        if not user:
            self.redirect("/login")
            return
        post = Post.get_by_id(long(post_id))
        cur_comment = Comment.get_by_id(long(comment_id))
        if (not post) or (not cur_comment):
            return self.redirect('/error')
        if user.key != cur_comment.author:
            self.logout()
            return self.redirect("/login")
        post_comments = Comment.query(Comment.for_post == post.key) \
                               .order(-Comment.created) \
                               .fetch()
        self.render("edit_comment.html", user=user, post=post,
                    comment_id=comment_id, current_comment=cur_comment,
                    comments=post_comments, post_id=post_id)

    def post(self, post_id, comment_id):
        title = self.request.get("subject")
        body = self.request.get("content")
        user = self.check_user_cookie("user_id")
        if not user:
            self.redirect("/login")
            return
        comment = self.request.get("comment_input")
        post = Post.get_by_id(long(post_id))
        if not post:
            return self.redirect('/error')
        if comment:
            c = Comment.get_by_id(long(comment_id))
            if user.key != c.author:
                self.logout()
                return self.redirect("/login")
            c.content = comment
            c.put()
            # Time.sleep() for eventual consistency of the database
            time.sleep(0.1)
            self.redirect("/singlepost/"+str(post_id))
            # self.redirect("/singlepost/" + str(post_id))
            return
        else:
            error = "We need some comment!"
            self.render("edit_comment.html", error_comment=error,
                        user=user, post=post, comment_id=comment_id,
                        current_comment=comment, post_id=post_id)

