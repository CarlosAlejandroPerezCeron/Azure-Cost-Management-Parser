import pandas as pd
from utils import log

def transform_cost_data(df):
    df["Date"] = pd.to_datetime(df["Date"])
    df["Cost"] = df["Cost"].astype(float)

    log("Calculating daily and cumulative costs...")

    daily = df.groupby(["Date", "Service"], as_index=False)["Cost"].sum()
    monthly = df.groupby("Service", as_index=False)["Cost"].sum().sort_values("Cost", ascending=False)

    return daily, monthly
