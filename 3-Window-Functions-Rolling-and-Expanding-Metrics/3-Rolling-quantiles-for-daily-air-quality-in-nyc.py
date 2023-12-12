# Resample, interpolate and inspect ozone data here
data = pd.read_csv('ozone.csv', parse_dates = ['date'], index_col = 'date')
data = data.resample('D').interpolate()
print(data.info())

# Create the rolling window
rolling = data['Ozone'].rolling(window = 360)

# Insert the rolling quantiles to the monthly returns
data['q10'] = rolling.quantile(0.1).to_frame('q10')
data['q50'] = rolling.quantile(0.5).to_frame('q50')
data['q90'] = rolling.quantile(0.9).to_frame('q90')

# Plot the data
data.plot()
plt.tight_layout(); plt.show()
