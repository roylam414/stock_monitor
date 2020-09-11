#import libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
import os.path
import time

def bot():	
	#panda format
	pd.options.display.float_format = '{:,.2f}'.format
	
	#import stock portfolio
	dirname = os.path.dirname(__file__)
	fullpath = os.path.join(dirname, '.\stock_portfolio.xlsx')
	df = pd.read_excel(fullpath)
	
	#format of stock protoflio
	df['no_of_shares'] = df['no_of_shares'].astype(float).round(-1)
	df['date_in'] = pd.to_datetime(df['date_in'])
	
	#Stock list for scraping loop
	stock_list = df.stock_code
	
	#webdriver setup
	chrome_options = Options()
	chrome_options.add_argument('--headless')
	
	
	#Create empty array for scraping info
	col_name = []
	col_last = []
	col_volume = []
	today = []
	
	
	#start the scraping loop
	for i in stock_list:
	    #Get request from HKEx.com.hk
	    driver = webdriver.Chrome('.\chromedriver.exe',options=chrome_options)
	    r = driver.get("https://www.hkex.com.hk/Market-Data/Securities-Prices/Equities/Equities-Quote?sym={}&sc_lang=en"\
	                    .format(i))
	    content = driver.page_source
	    soup = BeautifulSoup(content,'html.parser')
	
	    #Scraping the infor and append to array
	    ##Company name
	    col_name.append(soup.find('p', class_='col_name').get_text())
	    ##Lastest price
	    col_last.append(float(soup.find('span', class_='col_last').get_text()))
	    ##Volume
	    x = soup.find('dt', class_='ico_data col_volume').get_text()
	    replace = {'K':"1000",'M':"1000000",'B':"1000000000"}
	    for a in replace:
	        if x.find(a) == -1:
	            continue
	        
	        y = float(x.replace(a,"")) * float(replace[a])
	    col_volume.append(float(y))
	    ##Checking date
	    today.append(date.today())
	    
	    #Close the webdriver for running it again in the next loop
	    driver.close()
	
	#Gain/loss calculations
	change = col_last - df['cost_per_share']
	percent_change = ((change/df['cost_per_share'])*100)
	total_cost = df['cost_per_share'] * df.no_of_shares
	total_gain = change * df.no_of_shares
	##aging = today - df['date_in'] -----> not success
	
	#New dataframe for display
	df_column = dict([
	                ('stock_code',df.stock_code), 
	                ('col_name' , col_name), 
	                ('col_last' , col_last), 
	                ('cost_per_share' , df['cost_per_share']),
	                ('change' , change), 
	                ('percent_change', percent_change),
	                ('total_cost' , total_cost),
	                ('total_gain' , total_gain)               
	])
	df2 = pd.DataFrame(df_column)
	
	#Print the new dataframe in the console, it can output to an excel but it is not quite handy
	print(time.ctime())	
	with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'expand_frame_repr', False):  # more options can be specified also
	    print(df2)
	

