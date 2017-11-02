from .engine import Engine


class HeaderEngine(Engine):

    def render(self, fd, data):
        fd.write('\\documentclass[a4paper]{article}\n')
        fd.write('\\usepackage{geometry}\n')
        fd.write('\\geometry{left=2cm,right=2cm,top=2.5cm,bottom=2.5cm}\n')
        fd.write('\\usepackage{tikz}\n')
        fd.write('\\usepackage{float}\n')
        fd.write('\\usepackage{pgfplots}\n')
        fd.write('\\usepackage{xeCJK}\n')
        fd.write('\\usepackage[pdftitle={%s},pdfauthor={%s}]{hyperref}\n' %
                 (data['title'], data['author']))
        fd.write('\\title{%s}\n' % (data['title'], ))
        fd.write('\\author{%s}\n' % (data['author'], ))
        fd.write('\\date{%s}\n' % (data['date'], ))
        fd.write('\\begin{document}\n')
        fd.write('\\maketitle\n')
