from .engine.engine_factory import EngineFactory

import datetime
import pytz
import subprocess
import tempfile


class Reporter(object):

    def report(self, data):
        route = tempfile.mkdtemp()
        filename = 'main.tex'
        f = open(route + '/' + filename, 'w')
        self.create(f, data)
        f.close()
        return self.compile(route, filename)

    def create(self, fd, data):
        factory = EngineFactory()
        title = data.get('title', 'Report')
        author = data.get('author', 'TexReporter')
        date = datetime.datetime.now(pytz.utc).strftime('%Y-%m-%d %H:%M %z')
        date = data.get('date', date)
        factory.create('header').render(fd, {'title': title, 'author': author,
                                             'date': date})
        for item in data.get('data', []):
            factory.create(item.get('name')).render(fd, item.get('data'))
        factory.create('footer').render(fd)

    def compile(self, route, filename):
        command = ['xelatex', '-halt-on-error', '-output-directory=' + route,
                   route + '/' + filename]
        subprocess.call(command)
        return route + '/' + '.'.join(filename.split('.')[:-1]) + '.pdf'


if __name__ == '__main__':
    r = Reporter()
    data = {
        'data': [{
                'name': 'section',
                'data': {
                    'title': 'result',
                    'data': [{
                            'name': 'plot',
                            'data': [
                                (0, 4), (1, 1), (2, 2), (3, 5), (4, 6), (5, 1)
                            ]
                        }, {
                            'name': 'table',
                            'data': {
                                'column': 3,
                                'header': ('name', 'address', 'tel'),
                                'rows': [
                                    (1, 2, 3), (1, 2)
                                ]
                            }
                        }, {
                            'name': 'bar',
                            'data': {
                                'team1': 100,
                                2: 200,
                                'team final': 300
                            }
                        }
                    ]
                }
            }
        ]
    }
    print(r.report(data))
