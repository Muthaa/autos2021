import mechanicalsoup
import os

pg = mechanicalsoup.StatefulBrowser()
pg.open('https://biznakenya.com/top-100-companies-kenya/')

lst = pg.page.find_all("ol")
cln = [value for value in lst]
#for li in lst:
	#print value.text
with open("lst.csv", 'a+') as file:
	file.write(str(cln))
#print (cln)