# stock_monitor
Track the latest stock price and the gain/loss (for Hong Kong stock only!)

I is a webscraping exercise for me, but I found it quite useful later. 
Sometimes when I was working, it is not so handy to check my phone's stock trading app or login to the e-broking website.
This code allows me to check the stock price and my unrealised gain/loss at any time quickly.

Two problems I am facing are: 
1.  I think it is a little bit slow if I start and close the webdrive everytime for each stock in the loop.
    If there are hundreds of stock code in the loop, I think it will be no longer quick any more.
2.  Becoz I want to calculate the number of days I bought for each stock, but I havent figured out how the timestamp/
    datetime works in python, will be fixed later.

Target improvement:
1.  Setup a sorting function to push the most profit/loss making stock on the top line 
2.  Calculate the aging of each stock
3.  Maybe add EPS/PE/PB for reference, need to consider the necessity
