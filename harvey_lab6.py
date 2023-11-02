# Jackson Harvey, 10/6/2023, CS 135, Lab 6
# Adding more comments after uploading this file to GitHub on 10/24/23 for Lab 8
# This is an exercise to familiarize with committing changes locally
# Am now pushing this file to repository

import matplotlib.pyplot as plt
import numpy as np

plt.title("Jackson Harvey - Lab 6")

x,ct,cons,avh,gp,debt = np.loadtxt("lab6.csv", delimiter = ",", unpack=True)

# Count is given value ct. Is just a placeholder

plt.plot(x,cons, color="darkolivegreen", linestyle="solid", linewidth=2,
label="CPI")

plt.plot(x,avh, color="tan", linestyle="solid", linewidth=2,
label="Average Home Cost")

plt.plot(x,gp, color="darkorange", linestyle="solid", linewidth=2,
label="Gold Price")

# Limiting the range to keep the debt line
# from dwarfing the other lines
plt.ylim(0,3000)

plt.plot(x,debt, color="red", linestyle="solid", linewidth=2,
label="National Debt")

plt.xlabel("Years")
plt.ylabel("Adjusted Dollars - $")
plt.grid()

plt.legend()
plt.show()
