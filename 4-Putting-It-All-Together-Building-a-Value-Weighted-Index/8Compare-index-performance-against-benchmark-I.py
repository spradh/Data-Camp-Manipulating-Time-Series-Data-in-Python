# Convert index series to dataframe here
data = index.to_frame(name = 'Index')
print(data)


# Normalize djia series and add as new column to data
djia_norm = (djia/djia[0]) * 100
data['DJIA'] = djia
print(djia_norm)

# Show total return for both index and djia
print(data.iloc[-1].div(data.iloc[1]).sub(-1).mul(100))

# Plot both series
data.plot()
plt.tight_layout(); plt.show()
