import pandas as pd
import os
from datetime import datetime

# Configuration
REPORT_PATH = "/home/bloxperts/menuforge/outreach/runs/2026-05-05_outreach_report.csv"
METRICS_LOG = "/home/bloxperts/menuforge/outreach/engagement_metrics.csv"

def aggregate_metrics():
    if not os.path.exists(REPORT_PATH):
        print(f"Error: Report file {REPORT_PATH} not found.")
        return

    df = pd.read_csv(REPORT_PATH)
    
    # Basic counts
    total_sent = len(df)
    success_count = df['status'].str.contains('SUCCESS', na=False).sum()
    failure_count = total_sent - success_count
    
    # Prepare metrics row
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    metrics_row = {
        "timestamp": timestamp,
        "batch_size": total_sent,
        "success_rate": f"{(success_count/total_sent)*100:.2f}%" if total_sent > 0 else "0%",
        "success_count": success_count,
        "failure_count": failure_count
    }
    
    # Append to permanent log
    log_exists = os.path.exists(METRICS_LOG)
    log_df = pd.DataFrame([metrics_row])
    log_df.to_csv(METRICS_LOG, mode='a', index=False, header=not log_exists)
    
    print(f"Metrics updated in {METRICS_LOG}")
    print(f"Processed {total_sent} records. Success: {success_count}, Failure: {failure_count}")

if __name__ == "__main__":
    aggregate_metrics()
