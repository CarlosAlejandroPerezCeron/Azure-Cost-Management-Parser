import os
import matplotlib.pyplot as plt
from utils import log

def export_reports(daily, monthly, output_dir="./reports"):
    os.makedirs(output_dir, exist_ok=True)
    daily_path = os.path.join(output_dir, "daily_report.csv")
    monthly_path = os.path.join(output_dir, "monthly_summary.csv")

    daily.to_csv(daily_path, index=False)
    monthly.to_csv(monthly_path, index=False)

    log(f"Reports exported: {daily_path}, {monthly_path}")

    plt.figure(figsize=(10, 5))
    plt.bar(monthly["Service"], monthly["Cost"])
    plt.xticks(rotation=45, ha="right")
    plt.title("Azure Cost by Service")
    plt.ylabel("Cost (USD)")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "monthly_chart.png"))
    log("Chart saved as monthly_chart.png")
