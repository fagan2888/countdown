#!/usr/bin/env python

# Expects Python 3.*
# See https://www.campaignmonitor.com/css/ for email client CSS support

from datetime import date
from yattag import Doc, indent

dates = [{'title': 'Qual', 'date': date(2016, 1, 18)},
         {'title': 'NSF', 'date': date(2015, 10, 30)},
         {'title': 'Paris', 'date': date(2015, 12, 19)}]

# Generate an HTML document
doc, tag, text = Doc().tagtext()
doc.asis('<!DOCTYPE html>')

with tag('html'):
    with tag('body',
             style = 'font-family:"Palatino Linotype", "Book Antiqua", Palatino, serif;'):
        with tag('div', style = 'padding-left:15px;'):
            with tag('h1'):
                text('Things to Look Forward To')
        
            # Construct date objects
            today = date.today()
            for d in dates:
                d['d'] = (d['date'] - today).days
                d['datestr'] = d['date'].strftime('%Y-%m-%d')
            # Sort chronologically
            dates = sorted(dates, key=lambda k: k['date'])
        
            with tag('table'):
                for d in dates:
                    with tag('tr'):
                        with tag('td'):
                            doc.asis('&bull; ')
                            with tag('b'):
                                text(format(d['title']))
                        with tag('td', style = 'padding:0px 15px;'):
                            text('{0} days'.format(d['d']))
                        with tag('td'):
                            text('({0})'.format(d['datestr']))

print(indent(doc.getvalue()))
