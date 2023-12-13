# Import numpy
import numpy as np

# Define a multi_period_return function
def multi_period_return(period_returns):
    return np.prod(period_returns+1)-1
    
# Calculate daily returns
daily_returns = data.pct_change()

# Calculate rolling_annual_returns
rolling_annual_returns = daily_returns.rolling(window = '360D').apply(multi_period_return)

# Plot rolling_annual_returns
rolling_annual_returns.plot()
plt.tight_layout(); plt.show()
