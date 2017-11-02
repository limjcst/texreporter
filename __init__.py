def gen_section(data, title=None):
    assert isinstance(data, list), 'section data is not a list instance'
    return dict(data={'title': title, 'data': data}, name='section')


def gen_bar(data):
    assert isinstance(data, dict), 'bar data is not a dict instance'
    return dict(data=data, name='bar')


def gen_plot(data):
    assert isinstance(data, list), 'plot data is not a list instance'
    return dict(data=data, name='plot')


def gen_table(data, header):
    assert isinstance(data, list), 'table data is not a list instance'
    column = max([len(item) for item in data] + [len(header), ])
    return dict(data={'column': column, 'header': header, 'rows': data},
                name='table')
