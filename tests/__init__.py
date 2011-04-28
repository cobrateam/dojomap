class Environment(object):
    """Dummy class for data storage"""
    pass

env = Environment()

get_url = lambda path: "http://localhost:8080/%s" % path.lstrip("/")
