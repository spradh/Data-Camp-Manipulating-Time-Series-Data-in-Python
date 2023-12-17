# Select largest company for each sector
components = listings.groupby('Sector')["Market Capitalization"].nlargest(n = 1)


# Print components, sorted by market cap
print(components.sort_values(ascending = False))

# Select stock symbols and print the result
tickers = components.index.get_level_values("Stock Symbol")
print(tickers)

# Print company name, market cap, and last price for each component 
info_cols = listings.loc[tickers, ['Company Name', 'Market Capitalization', 'Last Sale']]
print(info_cols.sort_values(by = ['Market Capitalization'], ascending = False))
