# Import and inspect ozone data here
data = pd.read_csv('ozone.csv', parse_dates = ['date'], index_col = 'date').dropna()
print(data.info())

# Calculate the rolling mean and std here
rolling_stats = data.Ozone.rolling(window = 360).agg(['mean', 'std'])
print(rolling_stats.info())

# Join rolling_stats with ozone data
stats = data.join(rolling_stats)

# Plot stats
stats.plot(subplots = True)
plt.tight_layout(); plt.show()

