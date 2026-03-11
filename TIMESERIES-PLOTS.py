# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def ddmm2dd(ddmm):
    thedeg = np.floor(ddmm/100.)
    themin = (ddmm - thedeg*100.)/60.
    return thedeg + themin

# Load the CSV file and use the time column as index
df = pd.read_csv("SAA2_WC_2017_metocean_10min_avg.csv", parse_dates=['TIME_SERVER'], index_col=['TIME_SERVER'], na_values=['NULL'])

# Convert coordinates from ddmm to decimal degrees
df['LATITUDE_dd'] = ddmm2dd(df['LATITUDE'])
df['LONGITUDE_dd'] = ddmm2dd(df['LONGITUDE'])

# Select data up to 2017-07-04
df_selected = df.loc[:'2017-07-04']

#Plotting timeseries of temperature
plt.style.use('grayscale')
plt.figure(figsize=(10,5))
plt.plot(df_selected.index, df_selected['AIR_TEMPERATURE'], label='Air Temperature')
plt.xlabel('Time')
plt.ylabel('Air Temperature (°C)')
plt.title('Time Series of Air Temperature')
plt.legend()
plt.tight_layout()
plt.savefig('temperature_timeseries.png')
plt.show()

#Plotting Histrogram of Salinity
plt.figure(figsize=(8,5))
plt.hist(df_selected['TSG_SALINITY'].dropna(), bins=np.arange(30, 35.5, 0.5))
plt.xlabel('Salinity (PSU)')
plt.ylabel('Frequency')
plt.title('Histogram of Salinity')
plt.tight_layout()
plt.savefig('salinity_histogram.png')
plt.show()

#Printing statistics table
temp_mean = df_selected['AIR_TEMPERATURE'].mean()
temp_std = df_selected['AIR_TEMPERATURE'].std()
temp_iqr = df_selected['AIR_TEMPERATURE'].quantile(0.75) - df_selected['AIR_TEMPERATURE'].quantile(0.25)

sal_mean = df_selected['TSG_SALINITY'].mean()
sal_std = df_selected['TSG_SALINITY'].std()
sal_iqr = df_selected['TSG_SALINITY'].quantile(0.75) - df_selected['TSG_SALINITY'].quantile(0.25)

stats_table = pd.DataFrame({
    'Variable': ['Temperature', 'Salinity'],
    'Mean': [temp_mean, sal_mean],
    'Std Dev': [temp_std, sal_std],
    'IQR': [temp_iqr, sal_iqr]
})
print(stats_table)

#plottinga a scatter plot: wind speed vs temperature
plt.figure(figsize=(8,6))
sc = plt.scatter(
    df_selected['WIND_SPEED_TRUE'],
    df_selected['AIR_TEMPERATURE'],
    c=df_selected['LATITUDE_dd'],  # <-- fixed here
    cmap='viridis',
    edgecolor='k'
)
plt.colorbar(sc, label='Latitude (°)')
plt.xlabel('Wind Speed (m/s)')
plt.ylabel('Air Temperature (°C)')
plt.title('Wind Speed vs Air Temperature')
plt.tight_layout()
plt.savefig('wind_vs_temp.png', dpi=300)
plt.show()