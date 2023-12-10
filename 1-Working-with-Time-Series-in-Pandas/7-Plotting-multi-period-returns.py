# Create daily_return
google['daily_return'] = google['Close'].pct_change().mul(100)

# Create monthly_return
google['monthly_return'] =  google['Close'].pct_change(periods = 30).mul(100)

# Create annual_return
google['annual_return'] = google['Close'].pct_change(periods = 360).mul(100)

# Plot the result
google.plot(subplots=True)
plt.tight_layout(); plt.show()
