# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import cgi
import re
import time
import datetime

import webapp2
import jinja2


# Entities
from models import User
from models import Comment
from models import Post


# All Handlers
from handlers import *


class MainPage(Handler):
    def get(self):
        posts = Post.query().order(-Post.created).fetch()
        user = self.check_user_cookie("user_id")
        params_home = dict(posts=posts)
        params_home["body"] = ""
        params_home["error"] = ""
        params_home["user"] = user
        self.render("home.html", **params_home)


app = webapp2.WSGIApplication([
                              ('/newpost', CreatePost),
                              ('/signup', SignupHandler),
                              ('/registered', ValidPage),
                              ('/login', LoginHandler),
                              ('/logout', LogoutHandler),
                              ('/error', ErrorHandler),
                              ('/post-stats-update/', PostStatsUpdate),
                              (r'/singlepost/(\d+)', SinglePost),
                              (r'/edit-post/(\d+)', EditPost),
                              (r'/delete-post/(\d+)', DeletePost),
                              (r'/edit-comment/(\d+)/(\d+)', EditComment),
                              (r'/delete-comment/(\d+)/(\d+)', DeleteComment),
                              ('/', MainPage)
                              ], debug=True)
