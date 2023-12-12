# Inspect data here
print(monthly.info())

# Create weekly dates
weekly_dates = pd.date_range(start = monthly.index.min(), end = monthly.index.max(), freq = 'W')


# Reindex monthly to weekly data
weekly = monthly.reindex(weekly_dates)

# Create ffill and interpolated columns
weekly['ffill'] = weekly['UNRATE'].ffill()
weekly['interpolated'] = weekly['UNRATE'].interpolate()

# Plot weekly
weekly.plot()
plt.tight_layout(); plt.show()
