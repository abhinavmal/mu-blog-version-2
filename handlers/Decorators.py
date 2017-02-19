from functools import wraps
from models import *

# Decorators for checking if objects exist or not
def post_exists(function):
    @wraps(function)
    def wrapper(self, post_id, comment_id=None):
        post = Post.get_by_id(long(post_id))
        if post:
            return function(self, post_id, post)
        else:
            self.redirect('/error')
            return
    return wrapper

def comment_exists(function):
    @wraps(function)
    def wrapper(self, post_id=None, comment_id=None):
        comment = Comment.get_by_id(long(comment_id))
        post = Post.get_by_id(long(post_id))
        if comment and post:
            return function(self, post_id, comment_id, post, comment)
        else:
            self.redirect('/error')
            return
    return wrapper
# End of decorators
