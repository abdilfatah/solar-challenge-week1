import pandas as pd
import numpy as np

def load_data(country):
    """Simulates loading solar radiation data per country."""
    np.random.seed(42)
    date_rng = pd.date_range(start="2024-01-01", periods=100, freq="D")
    df = pd.DataFrame({
        "Timestamp": date_rng,
        "GHI": np.random.randint(200, 400, size=100),
        "DNI": np.random.randint(300, 600, size=100),
        "DHI": np.random.randint(100, 250, size=100),
        "Country": country
    })
    return df

def compute_summary_stats(df):
    """Computes mean, median, and standard deviation for solar radiation metrics."""
    summary = df.describe().T[["mean", "50%", "std"]].rename(columns={"50%": "median"})
    return summary