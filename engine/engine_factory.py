from .engine import Engine
from .header_engine import HeaderEngine
from .footer_engine import FooterEngine
from .tikz_engine import *
from .table_engine import TableEngine

from collections import defaultdict


class EngineFactory(object):

    def create(self, name, depth=0):
        depth += 1
        if name == 'header':
            return HeaderEngine(depth)
        elif name == 'footer':
            return FooterEngine(depth)
        elif name == 'section':
            return SectionEngine(depth)
        elif name == 'bar':
            return BarEngine(depth)
        elif name == 'plot':
            return PlotEngine(depth)
        elif name == 'table':
            return TableEngine(depth)
        else:
            return Engine(depth)


class SectionEngine(Engine):

    sectioning = {0: 'document', 1: 'section', 2: 'subsection',
                  3: 'subsubsection'}
    sectioning = defaultdict(lambda: 'paragraph', sectioning)

    def render(self, fd, data={}):
        fd.write('\\%s{%s}\n' % (self.sectioning[self.depth],
                                 self.to_string(data.get('title'))))
        factory = EngineFactory()
        for section in data.get('data', []):
            factory.create(section.get('name'), self.depth)\
                   .render(fd, section.get('data'))
