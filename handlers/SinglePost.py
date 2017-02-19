import time
from Handler import Handler
from Decorators import post_exists
from models import *


class SinglePost(Handler):
    @post_exists
    def get(self, post_id, post):
        user = self.check_user_cookie("user_id")
        post_comments = Comment.query(Comment.for_post == post.key) \
                               .order(-Comment.created) \
                               .fetch()
        author_is_user = False
        if user and post.author == user.key:
            author_is_user = True
            print "username_From_key", user.key.get().username
        self.render("single_post.html", post=post, post_id=str(post_id),
                    user=user, comments=post_comments,
                    author_is_user=author_is_user)

    @post_exists
    def post(self, post_id, post):
        user = self.check_user_cookie("user_id")
        if not user:
            self.redirect("/login")
            return
        comment = self.request.get("comment_input")
        post_comments = Comment.query(Comment.for_post == post.key) \
                               .order(-Comment.created) \
                               .fetch()
        author_is_user = False
        if post.author == user.key:
            author_is_user = True
        if not comment:
            error_comment = "We need some text in comment!"
            self.render("single_post.html", post=post, post_id=str(post_id),
                        user=user, comments=post_comments,
                        author_is_user=author_is_user,
                        error_comment=error_comment)
            return
        new_comment = Comment(author=user.key, content=comment,
                              for_post=Post.get_by_id(long(post_id)).key)
        comm_key = new_comment.put()
        # Time.sleep() for eventual consistency of the database
        time.sleep(0.5)
        # I redirected so that if the user refreshes, it calls the GET function
        # and not POST function. There is a return after redirect because
        # it may not stop execution by itself
        self.redirect("/singlepost/" + str(post_id))
        return
