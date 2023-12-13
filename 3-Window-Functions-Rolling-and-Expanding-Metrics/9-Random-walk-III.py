# Select fb start price here
start = fb.price.first('D')

# Add 1 to random walk and append to start
random_walk = 1 + random_walk
random_price = start.append(random_walk)

# Calculate cumulative product here
random_price = random_price.cumprod()

# Insert into fb and plot
fb['random'] = random_price
fb.plot()
plt.tight_layout(); plt.show()


