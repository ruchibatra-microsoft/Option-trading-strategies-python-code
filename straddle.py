import numpy as np
import matplotlib.pyplot as plt
import seaborn

#Define parameters
# PNB stock price 
spot_price = 10026.25 
# Long put
strike_price_long_put = 10000 
premium_long_put = 1760.20
# Long call
strike_price_long_call = 10000 
premium_long_call = 2030.35
# Stock price range at expiration of the put
sT = np.arange(0,2*spot_price,1)



def call_payoff(sT, strike_price, premium):
  return np.where(sT > strike_price, sT - strike_price, 0) - premium
payoff_long_call = call_payoff (sT, strike_price_long_call, premium_long_call)



fig, ax = plt.subplots()

ax.spines['top'].set_visible(False) # Top border removed

ax.spines['right'].set_visible(False) # Right border removed

ax.spines['bottom'].set_position('zero') # Sets the X-axis in the center

ax.plot(sT,payoff_long_call,label='Long Call',color='r')

plt.xlabel('Stock Price')

plt.ylabel('Profit and loss')

plt.legend()

plt.show()
def put_payoff(sT, strike_price, premium):
  return np.where(sT < strike_price, strike_price - sT, 0) - premium 
payoff_long_put = put_payoff(sT, strike_price_long_put, premium_long_put)



fig, ax = plt.subplots()

ax.spines['top'].set_visible(False) # Top border removed

ax.spines['right'].set_visible(False) # Right border removed

ax.spines['bottom'].set_position('zero') # Sets the X-axis in the center

ax.plot(sT,payoff_long_put,label='Long Put',color='g')

plt.xlabel('Stock Price')

plt.ylabel('Profit and loss')

plt.legend()

plt.show()


payoff_straddle = payoff_long_call + payoff_long_put
print ("Max Profit: Unlimited")

print ("Max Loss:", min(payoff_straddle))



fig, ax = plt.subplots()

ax.spines['top'].set_visible(False) # Top border removed

ax.spines['right'].set_visible(False) # Right border removed

ax.spines['bottom'].set_position('zero') # Sets the X-axis in the center


ax.plot(sT,payoff_long_call,'--',label='Long Call',color='r')

ax.plot(sT,payoff_long_put,'--',label='Long Put',color='g')


ax.plot(sT,payoff_straddle,label='Straddle')

plt.xlabel('Stock Price', ha='left')

plt.ylabel('Profit and loss')

plt.legend()

plt.show()



