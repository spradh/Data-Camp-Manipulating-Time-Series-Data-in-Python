# Import data here
data = pd.read_csv('unemployment.csv', parse_dates = ['date'], index_col = 'date')

# Show first five rows of weekly series
print(data.asfreq('W').head())

# Show first five rows of weekly series with bfill option
print(data.asfreq('W', method = 'bfill').head())

# Create weekly series with ffill option and show first five rows
weekly_ffill = data.asfreq('W', method = 'ffill')
print(weekly_ffill.head())

# Plot weekly_fill starting 2015 here 
weekly_ffill.loc['2015':].plot()
plt.tight_layout(); plt.show()

