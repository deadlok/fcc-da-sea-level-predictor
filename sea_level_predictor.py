import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    
    #print(df)

    # Create scatter plot
    plt.figure(figsize=(10,5))
    plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level')
    ax = plt.gca()
    ax.set_xticks([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])

    # Create first line of best fit
    s_future = pd.Series(np.arange(df['Year'].max()+1, 2051))
    x_vals = df['Year']
    x_vals = pd.concat([x_vals, s_future], ignore_index=True)

    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    #print(result)
    abline(result.slope, result.intercept, x_vals, color='red' )

    # Create second line of best fit
    df_2000 = df[ df['Year'] >= 2000 ]
    #print(result_2000)
    result_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])

    s_future = pd.Series(np.arange(df_2000['Year'].max()+1, 2051))
    x_vals = df_2000['Year']
    x_vals = pd.concat([x_vals, s_future], ignore_index=True)
    abline(result_2000.slope, result_2000.intercept, x_vals, color='blue' )

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    #print(ax.get_lines()[0].get_xdata().tolist())
    #print(ax.get_lines()[0].get_ydata().tolist())

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


#Plot a line from slope and intercept    
def abline(slope, intercept, x_vals, color='black'):
    axes = plt.gca()

    y_vals = intercept + slope * x_vals

    #print("################")
    #print(x_vals)
    #print(y_vals)
    plt.plot(x_vals, y_vals, '--', color=color)