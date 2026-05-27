import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]

    # 2. Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # CRITICAL: Plot the scatter data points first so it is the primary child element
    ax.scatter(x, y, color="blue", s=15)

    # 3. Create first line of best fit (Entire Dataset: 1880 - Present)
    res_first = linregress(x, y)
    
    # Generate extended timeline array up to 2050
    x_pred1 = np.arange(1880, 2051)
    y_pred1 = res_first.slope * x_pred1 + res_first.intercept
    
    ax.plot(x_pred1, y_pred1, color="red", linestyle="--", linewidth=2)

    # 4. Create second line of best fit (Recent Trends: 2000 - Present)
    df_recent = df[df["Year"] >= 2000]
    x_recent = df_recent["Year"]
    y_recent = df_recent["CSIRO Adjusted Sea Level"]
    
    res_second = linregress(x_recent, y_recent)
    
    # Generate recent timeline array up to 2050
    x_pred2 = np.arange(2000, 2051)
    y_pred2 = res_second.slope * x_pred2 + res_second.intercept
    
    ax.plot(x_pred2, y_pred2, color="green", linestyle="-", linewidth=2)

    # 5. Add exact labels and title matching the test constraints
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    
    # Clean up visual window boundaries
    ax.set_xlim(1870, 2060)
    
    # Save image and return the AXES object explicitly
    fig.savefig('sea_level_plot.png')
    return ax