import pandas as pd
import quandl as qd 
import numpy as np 
import matplotlib.pyplot as plt

# pulls the trading API
try: 
    qd.ApiConfig.api_key = "s3STTXaAPLChArcTWH_o"
except:
    print("Cant pull API try again")

msft_data = qd.get("EDO/MSFT", start_date ="2020-01-01", end_date="2020-01-01")
msft_data.head()

#calaculates returns 
close_price = msft_data[['Adj_Close']]
daily_return = close_price.pct_change()
daily_return.fillna(0, inplace=True)
print(daily_return)


#moving averages
adj_price =msft_data['Adj_Close']
mav = adj_price.rolling(window=50).mean()
print(mav[-10:])

#plot and see/track difference 
adj_price.plot()
mav.plot()