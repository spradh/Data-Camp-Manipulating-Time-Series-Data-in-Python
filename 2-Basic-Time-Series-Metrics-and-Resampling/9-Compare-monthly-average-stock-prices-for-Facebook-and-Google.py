# Import and inspect data here
stocks = pd.read_csv('stocks.csv', index_col = 'date', parse_dates = ['date'])
print(stocks.info())

# Calculate and plot the monthly averages
monthly_average = stocks.resample('M').mean()
monthly_average.plot(subplots = True)
plt.tight_layout(); plt.show()

