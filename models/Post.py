# DB : ndb
from google.appengine.ext import ndb
from User import User
import datetime

# Time zone
import pytz


class Post(ndb.Model):
    """A set of attributes to describe the post
    """
    title = ndb.StringProperty(required=True)
    body = ndb.TextProperty(required=True)
    created = ndb.DateTimeProperty(auto_now=True)
    author = ndb.KeyProperty(kind=User)
    likes = ndb.KeyProperty(kind=User, repeated=True)
    dislikes = ndb.KeyProperty(kind=User, repeated=True)

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

    @property
    def num_likes(self):
        return len(self.likes)

    @property
    def num_dislikes(self):
        return len(self.dislikes)

    @property
    def author_name(self):
        return self.author.get().username