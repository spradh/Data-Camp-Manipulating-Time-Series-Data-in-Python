# Set seed here
seed(42)

# Calculate daily_returns here
daily_returns = fb.pct_change()

# Get n_obs
n_obs = daily_returns.count()

# Create random_walk
random_walk = choice(daily_returns, size = n_obs)

# Convert random_walk to pd.series
random_walk = pd.Series(random_walk)

# Plot random_walk distribution
random_walk.plot()
plt.tight_layout(); plt.show()
