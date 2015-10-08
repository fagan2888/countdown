#!/usr/bin/env python

# I expect Python 3.*!

from datetime import date
from yattag import Doc, indent

doc, tag, text = Doc().tagtext()

with tag('h1'):
    text('Welcome to the future')

dates = [{'title': 'Qual', 'date': date(2016, 1, 18)},
         {'title': 'NSF', 'date': date(2015, 10, 30)}]
today = date.today()

for d in dates:
    d['d'] = (d['date'] - today).days
    d['datestr'] = d['date'].strftime('%Y-%m-%d')
    
w_title = max([len(d['title']) for d in dates]) + 1
w_count = max([len(str(d['d'])) for d in dates])

with tag('ul'):
    for d in dates:
        with tag('li'):
            text('{0:{1}}: {2:{3}} days ({4})'
                 .format(d['title'], w_title,
                         d['d'], w_count,
                         d['datestr']
                     )
             )

print(indent(doc.getvalue()))
