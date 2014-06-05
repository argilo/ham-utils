# Copyright 2014 Clayton Smith (argilo@gmail.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import smtplib
from email.mime.text import MIMEText

def mail(text):
    gmail_sender = 'your.account@gmail.com'
    gmail_passwd = 'yourpassword'
    recipient = 'your.account@gmail.com'

    msg = MIMEText(text)

    msg['Subject'] = 'WSJT-X alert'
    msg['From'] = gmail_sender
    msg['To'] = recipient

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login(gmail_sender, gmail_passwd)
    s.sendmail(gmail_sender, [recipient], msg.as_string())
    s.quit()

import time, os

filename = 'C:\\wsjtx2\\ALL.TXT'
file = open(filename, 'r')

st_results = os.stat(filename)
st_size = st_results[6]
file.seek(st_size)

while True:
    where = file.tell()
    newstuff = file.read()
    if not newstuff:
        time.sleep(1)
        file.seek(where)
    else:
        mail(newstuff)

