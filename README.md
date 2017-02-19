# Responsive - Multi User Blog

This is the source code for a multi-user blog, hosted with the Google App Engine (GAE) at https://mu-blog-5551.appspot.com/.

- The blog allows users to create secure accounts (hashed passwords, secure cookies).

- Users can let their heart out without really the fear of disclosing their identity, it is an emotional outlet after a long day!

- Users can like/dislike and comment on other's posts (ONLY).

- Dependencies:

  - Frontent
    - jQuery
    - Bootstrap Library
    - Google Fonts


  - Backend
    - Jinja2 for templating
    - GAE Framework
    - NDB datastore
    - Hashlib and hmac for hashing
    - gae-pytz for setting time-zone

- To run this blog locally, simply clone the repository using:
  `git clone git@github.com:abhinavmal/mu-blog-version-2.git` 
  and run `dev_appserver.py .` from the directory which contains the file `app.yaml`.
