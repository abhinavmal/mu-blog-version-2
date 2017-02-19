# DB : ndb
from google.appengine.ext import ndb
from User import User
from Post import Post
import datetime

# Time zone
import pytz


class Comment(ndb.Model):
    """A set of attributes to describe the comments on posts
    """
    author = ndb.KeyProperty(kind=User)
    content = ndb.TextProperty()
    created = ndb.DateTimeProperty(auto_now=True)
    for_post = ndb.KeyProperty(kind=Post)

    def get_date(self, format='%B %d, %Y'):
        # return self.created.date().strftime(format)
        unaware_est = datetime.datetime.strptime(str(self.created),
                                                 "%Y-%m-%d %H:%M:%S.%f")
        # timeUTC = self.created.time().strftime(format)
        # http://stackoverflow.com/questions/18176148/converting-an-un-aware-timestamp-into-an-aware-timestamp-for-utc-conversion
        timezone_local = pytz.timezone("America/Chicago")
        utc = pytz.utc
        time_local = utc.localize(unaware_est).astimezone(timezone_local)
        return time_local.strftime(format)

    def get_time(self, format='%I:%M %p'):
        # Manipulation to bring it to Central Time US
        unaware_est = datetime.datetime.strptime(str(self.created),
                                                 "%Y-%m-%d %H:%M:%S.%f")
        # timeUTC = self.created.time().strftime(format)
        # http://stackoverflow.com/questions/18176148/converting-an-un-aware-timestamp-into-an-aware-timestamp-for-utc-conversion
        timezone_local = pytz.timezone("America/Chicago")
        utc = pytz.utc
        time_local = utc.localize(unaware_est).astimezone(timezone_local)
        return time_local.strftime(format)
