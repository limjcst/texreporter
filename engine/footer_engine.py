from .engine import Engine


class FooterEngine(Engine):

    def render(self, fd, data={}):
        fd.write('\\end{document}\n')
