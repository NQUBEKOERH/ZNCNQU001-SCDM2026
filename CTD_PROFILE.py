import pandas as pd
import matplotlib.pyplot as plt

# load data
df = pd.read_csv(
    r"C:\Users\zncnqu001\Downloads\P2\CTD_TEMP_SALINITY_PROFILE.dat",
    sep="\t"
)

depth = df["Depth"]
temperature = df["Temp"]
salinity = df["Salinity(psu)"]

# create two panels sharing y-axis
fig, ax = plt.subplots(1,2,sharey=True)

# temperature
ax[0].plot(temperature, depth, color="red")
ax[0].set_xlabel("Temperature (°C)")
ax[0].set_ylabel("Depth (m)")
ax[0].set_title("Temperature Profile")

# salinity
ax[1].plot(salinity, depth, color="blue")
ax[1].set_xlabel("Salinity (PSU)")
ax[1].set_title("Salinity Profile")

# invert depth axis
ax[0].invert_yaxis()

plt.tight_layout()
plt.show()
