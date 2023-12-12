# Import and inspect data here
ozone = pd.read_csv('ozone.csv', parse_dates = ['date'], index_col = 'date')
print(ozone.info())

# Calculate and plot the weekly average ozone trend
ozone.resample('W').mean().plot()
plt.tight_layout(); plt.show()

# Calculate and plot the monthly average ozone trend
ozone.resample('M').mean().plot()
plt.tight_layout(); plt.show()

# Calculate and plot the annual average ozone trend
ozone.resample('Y').mean().plot()
plt.tight_layout(); plt.show()
