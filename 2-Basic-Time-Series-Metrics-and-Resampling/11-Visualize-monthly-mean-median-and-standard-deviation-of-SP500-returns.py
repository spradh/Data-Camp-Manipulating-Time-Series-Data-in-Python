# Import data here
sp500 = pd.read_csv('sp500.csv', parse_dates = ['date'], index_col = 'date')

# Calculate daily returns here
daily_returns = sp500.squeeze().pct_change()

# Resample and calculate statistics
stats = daily_returns.resample("M").agg(['mean', 'median', 'std'])

# Plot stats here
stats.plot()
plt.tight_layout(); plt.show()
