#!/usr/bin/env python

# GMail may fail the first time you run this and suggest you login;
# visit https://support.google.com/mail/answer/78754
# before running this script and "allow less secure apps access to
# your account."
#
# Assumes variables `username` and `password` for GMail are set in a
# file `./secrets.py`.
# 
# Expects Python 3.*
# See https://www.campaignmonitor.com/css/ for email client CSS support

from datetime import date
from yattag import Doc, indent

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from secrets import username, password
sender = 'mhlinder@gmail.com'
recipient = 'mhlinder@gmail.com'
# Order doesn't matter
dates = [{'title': 'Qual', 'date': date(2016, 1, 18)},
         {'title': 'NSF', 'date': date(2015, 10, 30)},
         {'title': 'Paris', 'date': date(2015, 12, 19)}]

# Generate an HTML document
doc, tag, text = Doc().tagtext()
doc.asis('<!DOCTYPE html>')

with tag('html'):
    with tag('body',
             style = 'font-family:"Palatino Linotype", "Book Antiqua", Palatino, serif;color=black'):
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

            # Format dates into a table
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

# Format as a MIME object
msg = MIMEText(indent(doc.getvalue()), 'html')

msg['To'] = recipient
msg['From'] = sender
msg['Subject'] = 'Countdown {0}'.format(today.strftime('%Y-%m-%d'))

# Send with SMTP
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(sender, recipient, msg.as_string())
server.quit()

