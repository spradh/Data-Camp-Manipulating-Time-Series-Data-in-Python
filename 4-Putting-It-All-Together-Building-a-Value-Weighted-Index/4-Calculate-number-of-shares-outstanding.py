# Inspect listings and print tickers
print(listings.info())
print(tickers)

# Select components and relevant columns from listings
components = listings.loc[tickers, ["Market Capitalization", 'Last Sale']]

# Print the first rows of components
print(components.iloc[0])

# Calculate the number of shares here
no_shares = listings['Market Capitalization']/ listings['Last Sale']

# Print the sorted no_shares
print(no_shares.sort_values(ascending = False))
