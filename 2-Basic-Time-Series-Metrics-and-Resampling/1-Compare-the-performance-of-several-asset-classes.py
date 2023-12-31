# Import data here
prices = pd.read_csv("asset_classes.csv", index_col = 'DATE', parse_dates = ['DATE'])

# Inspect prices here
print(prices.info())

# Select first prices
first_prices = prices.iloc[0]

# Create normalized
normalized = prices.div(first_prices).mul(100)

# Plot normalized
normalized.plot()
plt.tight_layout(); plt.show()
