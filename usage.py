import requests # Requests library to retrieve HTML
from bs4 import BeautifulSoup # Beautiful Soup library to parse HTML
from Tkinter import *


def window(balance, limit, days_left):
 win = Tk()
 l1 = Label( win, text = 'Airtel Usage Statistics :')
 l1.grid(row = 0, column = 0)
 l2 = Label( win, text = 'Balance Data :')
 v2 = StringVar()
 v2.set(balance)
 e2 = Entry(win , textvariable = v2)
 l2.grid(row = 1, column = 0)
 e2.grid(row = 1, column = 1)
 l3 = Label( win, text = 'Data Limit :')
 v3 = StringVar()
 v3.set(limit)
 e3 = Entry( win , textvariable = v3)
 l3.grid(row = 2, column = 0)
 e3.grid(row = 2, column = 1)
 l4 = Label( win, text = 'Days Left :')
 v4 = StringVar()
 v4.set(days_left)
 e4 = Entry(win , textvariable = v4)
 l4.grid(row = 3, column = 0)
 e4.grid(row = 3, column = 1)
 win.mainloop()

response1 = requests.get('http://www.airtel.in/smartbyte-s/page.html')
page1 = response1.content
soup1 = BeautifulSoup(page1) 
sample1 = [x['src'] for x in soup1.find_all('iframe')] #iframe with external ip based link is loaded
sample2 = ''.join(sample1)

# external ip based link is requested
response2 = requests.get(sample2)
page2 = response2.content
soup2 = BeautifulSoup(page2)
sample4 = soup2.find('ul','list1 clearfix')
sample5 = sample4.find_all('span')

#parse and get following values
balance = sample5[1].text
DSLno = sample5[3].text
limit = sample5[0].text
days_left = sample5[2].text

window(balance, limit, days_left)
