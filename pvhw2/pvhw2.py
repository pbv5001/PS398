#Peter Vining python assignment 2
#program to manage stock portfolio

import random
import re
import urllib  #This integrates code from Corey Goldberg's blog, available at http://www.goldb.org/pythonwebscraping.html, into the function for stocks

class Portf(object):
  
  def __init__(self):
  
	self.transnumber= 0
	self.record=""
	self.cash= 0
	self.stocks= {}
	self.mutualfunds= {}
	
	
"""
  def currentholdings(self):
		print "Current cash balance is: $%d\n" %(self.cash) 
		FILE= open('record.txt','a')
		FILE.write("Current cash balance is: $%d\n" %(self.cash)) 
		for i in range(len(self.stocks)):
			print "stock holding %d is: %str \n" %(i, self.stocks)
			FILE.write("stock holding %d is: %str \n" %(i, self.stocks))
		for i in range (len(self.mutualfunds)):
			print "mutual fund holding %d is: %str \n" %(i, self.mutualfunds)
			FILE.write("mutual fund holding %d is: %str \n" %(i, self.mutualfunds))
		FILE.close()
  """
  def addcash(self, value):
	self.cash+= value
	self.transnumber += 1
	import datetime
	now = str(datetime.datetime.now())
	print "Transaction %d %str: Added $%d from account; new cash balance is $%d" %(self.transnumber, now, value, self.cash)
	FILE= open('history.txt','a')
	FILE.write("Transaction %d %str: Added $%d from account; new cash balance is $%d \n" %(self.transnumber, now, value, self.cash))
	FILE.close()
	FILE= open('history.csv','a') #CSV file version
	FILE.write("%d,%str,%d,%d\n" %(self.transnumber, now, value, self.cash))
	FILE.close()
	

		
  def withdrawcash(self, value):
	self.cash-= value
	self.transnumber += 1
	import datetime
	now = str(datetime.datetime.now())
	print "Transaction %d %str: Withdrew $%d from account; new cash balance is $%d" %(self.transnumber, now, value, self.cash)
	FILE= open('history.txt','a')
	FILE.write("Transaction %d %str: Withdrew $%d from account; new cash balance is $%d \n" %(self.transnumber, now, value, self.cash))
	FILE.close()
	FILE= open('history.csv','a')
	FILE.write("%d,%str,%d,%d\n" %(self.transnumber, now, value, self.cash))
	FILE.close()

	
  def addstock(self, ticker, shares):
	self.ticker=ticker
	self.shares=shares
	base_url = 'http://finance.google.com/finance?q='
	content = urllib.urlopen(base_url+ticker).read()
	m = re.search('<span\sid="ref_\w+_\w+">(\w+\.\w+)</span>', content) #This regex was tough to get right; the original code from 2007 didnt work because the HTML formatting had changed, and also because I didnt realize that the \d regex isnt supported by some older utilities, of which urllib seems to be one, so I went with \w instead
	if m:
		self.price = m.group(1)
	else:
		return 'no quote available for: ' + ticker
	self.price=float(self.price)
	if self.cash < self.price*self.shares:
		return "Your account balance is too low for this purchase"
	else:
		self.cash-=(self.price*self.shares)
		self.stocks[ticker]= ("%d %s" %(self.shares, self.ticker))
		self.transnumber += 1
		import datetime
		now = str(datetime.datetime.now())
		print "Transaction %d %str: %d shares of %s purchased at %d share price, new cash balance is %d" %(self.transnumber, now, self.shares, self.ticker, self.price, self.cash)
		FILE= open('history.txt','a')
		FILE.write("Transaction %d %str: Added %s shares of %s to account; new cash balance is $%d \n" %(self.transnumber, now, self.shares, self.ticker, self.cash))
		FILE.close()
		FILE= open('history.csv','a')
		FILE.write("%d,%str,%s,%d,%d\n" %(self.transnumber, now, self.ticker, self.shares, self.cash))
		FILE.close()

		
  def sellstock(self, ticker, shares):
	self.ticker=ticker
	self.shares=shares
	if self.shares <= self.stocks['%s'%(self.ticker)][0]:
		base_url = 'http://finance.google.com/finance?q='
		content = urllib.urlopen(base_url+ticker).read()
		m = re.search('<span\sid="ref_\w+_\w+">(\w+\.\w+)</span>', content) #This regex was tough to get right; the original code from 2007 didnt work because the HTML formatting had changed, and also because I didnt realize that the \d regex isnt supported by some older utilities, of which urllib seems to be one, so I went with \w instead
	else:
		print "Cannot complete transaction; stock holdings do not exist"
	if m:
		self.price = m.group(1)
	else:
		return 'no quote available for: ' + ticker
	self.price=float(self.price)
	self.cash+=(self.price*self.shares)
	self.stocks[ticker]= ("%s, %d)" %(self.ticker, self.shares))
	self.transnumber += 1
	import datetime
	now = str(datetime.datetime.now())
	print "Transaction %d $str: %d shares of %s sold at %d share price, new cash balance is %d" %(self.transnumber, now, self.shares, self.ticker, self.price, self.cash)
	FILE= open('history.txt','a')
	FILE.write("Transaction %d %str: Added %d shares of %s to account; new cash balance is $%d \n" %(self.transnumber, now, self.shares, self.ticker, self.cash))
	FILE.close()
	FILE= open('history.csv','a')
	FILE.write("%d,%str,%s,%d,%d\n" %(self.transnumber, now, self.ticker, self.shares, self.cash))
	FILE.close()
				
	
	
