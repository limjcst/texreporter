from .engine import Engine


class TableEngine(Engine):

    def render(self, fd, data):
        column = data.get('column', 1)
        fd.write('\\begin{table}[ht]\n')
        fd.write('\\begin{tabular}{%s}\n' % ('l' * column, ))
        fd.write('\\hline\n')
        fd.write('&'.join(self.to_strtuple(data.get('header', [])[:column])))
        fd.write('\\\\\n\\hline\n')
        for row in data.get('rows', []):
            fd.write('&'.join(self.to_strtuple(row[:column])))
            fd.write('\\\\\n')
        fd.write('\\hline\n')
        fd.write('\\end{tabular}\n')
        fd.write('\\end{table}\n')
