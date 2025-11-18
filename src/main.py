from fetch_cost_data import fetch_cost_data
from transform_cost_data import transform_cost_data
from export_reports import export_reports
from utils import log

def main():
    log("=== Azure Cost Management Parser ===")

    df = fetch_cost_data()
    daily, monthly = transform_cost_data(df)
    export_reports(daily, monthly)

    log("Pipeline completed successfully.")

if __name__ == "__main__":
    main()
