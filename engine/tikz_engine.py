from .engine import Engine


class TikzEngine(Engine):

    def render(self, fd, data):
        fd.write('\\begin{figure}[H]\n')
        fd.write('\\begin{tikzpicture}\n')
        self.draw(fd, data)
        fd.write('\\end{tikzpicture}\n')
        fd.write('\\end{figure}\n')


class BarEngine(TikzEngine):

    def draw(self, fd, data):
        keys = data.keys()
        ticks = '{%s}' % (','.join(self.to_strtuple(keys)), )
        fd.write('\\begin{axis}[xbar,'
                 'y axis line style = { opacity = 0 },'
                 'axis x line       = none,'
                 'tickwidth         = 0pt,'
                 'enlarge x limits  = 0.02,'
                 'symbolic y coords = %s,'
                 'ytick = %s,'
                 'nodes near coords,]\n' %
                 (ticks, ticks))
        fd.write('\\addplot\n')
        fd.write('coordinates {')
        for point in data:
            fd.write('(%s,%s) ' % self.to_strtuple([data[point], point]))
        fd.write('};\n')
        fd.write('\\end{axis}\n')


class PlotEngine(TikzEngine):

    def draw(self, fd, data):
        fd.write('\\begin{axis}\n')
        fd.write('\\addplot+[sharp plot]\n')
        fd.write('coordinates {')
        for point in data:
            fd.write('(%s,%s)' % self.to_strtuple([point[0], point[1]]))
        fd.write('};\n')
        fd.write('\\end{axis}\n')
