import matplotlib
import numpy as np

def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    d0 = x[-1]
    x -= d0
    coeffs = np.polyfit(x, levels, p)
    return np.poly1d(coeffs), d0