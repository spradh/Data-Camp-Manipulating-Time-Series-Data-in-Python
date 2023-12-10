# Import data here
google = pd.read_csv('google.csv', index_col = 'Date', parse_dates = ['Date'])
#print(google.info())

# Set data frequency to business daily
google = google.asfreq('B')

# Create 'lagged' and 'shifted'
google['lagged'] = google["Close"].shift(periods = -90)
google['shifted'] = google["Close"].shift(periods = 90)

# Plot the google price series
google.plot(subplots=True)
plt.tight_layout(); plt.show()

