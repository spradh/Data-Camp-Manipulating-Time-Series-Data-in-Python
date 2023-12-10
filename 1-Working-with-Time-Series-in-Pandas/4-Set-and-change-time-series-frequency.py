# Inspect data
print(co.info())

# Set the frequency to calendar daily
co = co.asfreq('D')

# Plot the data
co.plot(subplots=True)
plt.tight_layout(); plt.show()


# Set frequency to monthly
co = co = co.asfreq('M')

# Plot the data
co.plot(subplots=True)
plt.tight_layout(); plt.show()
