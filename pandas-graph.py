# Created 24 July 2017
import pandas as pd
import matplotlib.pyplot as plt


# Revenue values list
revenue = [2.5, 3.5, 4.5, 5.5]

# Operational costs list
opCost = [1.5, 2.1, 2.5, 3.0]

# Year value list
year = [2013, 2014, 2015, 2016]

revenueCostDF = pd.DataFrame(
    {
        "Revenue" : revenue,
        "Operational Cost" : opCost,
        "Year" : year
    }

)

# Printing dataframe
print(revenueCostDF)

# Plot the revenue chart
#revenueCostDF.plot(x="Year", y="Revenue")

revenueCostDF.plot(
    x="Year",
    y=["Revenue", "Operational Cost"],
    kind="barh",
    title="Revenue vs Cost",
    colormap="plasma")
plt.show()
