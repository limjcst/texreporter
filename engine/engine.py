class Engine(object):

    def __init__(self, depth=0):
        self.depth = depth

    def render(self, fd, data):
        fd.write('%s\n' % (str(data), ))

    @classmethod
    def to_strtuple(cls, l):
        return tuple([cls.to_string(str(item)) for item in l])

    @classmethod
    def to_string(cls, s):
        if not isinstance(s, str):
            return s
        s = s.replace('\\', '\\\\')
        s = s.replace('_', '\\_')
        return s
