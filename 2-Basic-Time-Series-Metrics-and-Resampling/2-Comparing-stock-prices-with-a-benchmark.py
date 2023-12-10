# Import stock prices and index here
stocks = pd.read_csv('nyse.csv', parse_dates = ['date'], index_col = 'date')
dow_jones = pd.read_csv('dow_jones.csv', parse_dates = ['date'], index_col = 'date')

# Concatenate data and inspect result here
data = pd.concat([stocks, dow_jones], axis = 1)
print(data.info())

# Normalize and plot your data here
data.div(data.iloc[0]).mul(100).plot()
plt.tight_layout(); plt.show()

