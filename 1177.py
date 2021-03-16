import requests

from bs4 import BeautifulSoup

import time

import smtplib, ssl

port = 465

smtp_server = 'smtp.gmail.com'

sender_email = ''

receiver_email = ['', '']

password = ''

URL = 'https://www.1177.se/Orebrolan/sjukdomar--besvar/lungor-och-luftvagar/inflammation-och-infektion-ilungor-och-luftror/om-covid-19--coronavirus/om-vaccin-mot-covid-19/vaccination-mot-covid-19-region-orebro-lan/'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('li')[39]

age = 18

a = 0

while a < 1:
 for result in results:
  if age == 80:
   age = 18
   time.sleep(1800) 
  if int(result[10:12]) == age:
   a = 2
 age +=1
age -=1
sage = str(age)

message = '''\
Amne: Coronavaccin

Aldern for coronavaccinet har andrats till ''' + sage + '!'

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
