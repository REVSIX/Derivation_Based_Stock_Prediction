import numpy as np
from sklearn.metrics import mean_squared_error

def fit_and_evaluate(x, y, degree):
    coeffs = np.polyfit(x, y, degree)
    p = np.poly1d(coeffs)
    y_pred = p(x)
    mse = mean_squared_error(y, y_pred)
    return coeffs, p, mse

def find_extrema(p, dp, d2p, x_min, x_max, n_points=1000):
    x_vals = np.linspace(x_min, x_max, n_points)
    y_vals = dp(x_vals)
    
    # Find where the derivative changes sign
    sign_changes = np.where(np.diff(np.sign(y_vals)))[0]
    
    extrema = []
    for idx in sign_changes:
        x_extremum = (x_vals[idx] + x_vals[idx + 1]) / 2
        y_extremum = p(x_extremum)
        if d2p(x_extremum) > 0:
            extremum_type = "Minimum"
        elif d2p(x_extremum) < 0:
            extremum_type = "Maximum"
        else:
            extremum_type = "Inflection point"
        
        extrema.append((x_extremum, y_extremum, extremum_type))
    
    return extrema