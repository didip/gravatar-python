class Gravatar:
  root_url = "http://www.gravatar.com/avatar.php"

  def __init__(self, email, default, size):
    self.email = email
    self.default = default
    self.size = size
    self.gravatar_id = self.gravatar_id()
    self.gravatar_url = self.gravatar_url()

  def gravatar_id(self):
    import hashlib
    return hashlib.md5(self.email.lower()).hexdigest()

  def gravatar_url(self):
    import urllib
    return "%s?%s" % (self.__class__.root_url, urllib.urlencode(self.__dict__))
