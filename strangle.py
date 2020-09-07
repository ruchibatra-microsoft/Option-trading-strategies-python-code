import numpy as np
import matplotlib.pyplot as plt
import seaborn
# Fortis stock price 
spot_price = 9907.55
# Long put

strike_price_long_put = 9800

premium_long_put = 1660.00


# Long call

strike_price_long_call = 10000 

premium_long_call = 1420.45


# Stock price range at expiration of the put

sT = np.arange(0,2*spot_price,1)


def call_payoff(sT, strike_price, premium):
  return np.where(sT > strike_price, sT - strike_price, 0)-premium

payoff_long_call = call_payoff(sT, strike_price_long_call, premium_long_call)
# Plot

fig, ax = plt.subplots()

ax.spines['bottom'].set_position('zero')

ax.plot(sT,payoff_long_call,label='Long Call',color='r')

plt.xlabel('Stock Price')

plt.ylabel('Profit and loss')

plt.legend()

plt.show()


def put_payoff(sT, strike_price, premium):
  return np.where(sT < strike_price, strike_price - sT, 0) - premium

payoff_long_put = put_payoff(sT, strike_price_long_put, premium_long_put)
# Plot

fig, ax = plt.subplots()

ax.spines['bottom'].set_position('zero')

ax.plot(sT,payoff_long_put,label='Long Put',color='g')

plt.xlabel('Stock Price')

plt.ylabel('Profit and loss')

plt.legend()

plt.show()




payoff_strangle = payoff_long_call + payoff_long_put
print ("Max Profit: Unlimited")

print ("Max Loss:", min(payoff_strangle))


# Plot

fig, ax = plt.subplots()

ax.spines['bottom'].set_position('zero')


ax.plot(sT,payoff_long_call,'--',label='Long Call',color='r')

ax.plot(sT,payoff_long_put,'--',label='Long Put',color='g')


ax.plot(sT,payoff_strangle,label='Strangle')

plt.xlabel('Stock Price')

plt.ylabel('Profit and loss')

plt.legend()

plt.show()

