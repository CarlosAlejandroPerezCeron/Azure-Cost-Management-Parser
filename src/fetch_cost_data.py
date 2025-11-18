import os
import datetime
import pandas as pd
from azure.mgmt.costmanagement import CostManagementClient
from utils import get_credentials, log

def fetch_cost_data():
    creds = get_credentials()
    client = CostManagementClient(credential=creds)

    subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=int(os.getenv("PERIOD_DAYS", 7)))

    log(f"Fetching cost data from {start_date} to {end_date}...")

    report = client.query.usage(
        scope=f"/subscriptions/{subscription_id}",
        parameters={
            "type": "Usage",
            "timeframe": "Custom",
            "timePeriod": {"from": str(start_date), "to": str(end_date)},
            "dataset": {
                "granularity": "Daily",
                "aggregation": {"totalCost": {"name": "PreTaxCost", "function": "Sum"}},
                "grouping": [{"type": "Dimension", "name": "ServiceName"}]
            }
        }
    )

    rows = [item["metric"]["totalCost"] for item in report.rows]
    df = pd.DataFrame(report.rows, columns=["Date", "Service", "Cost"])
    return df

if __name__ == "__main__":
    df = fetch_cost_data()
    print(df.head())
