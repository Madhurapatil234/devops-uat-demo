
import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

# Load the sample dataset
reference_data = pd.read_csv("uat_data.csv")

# Create changed data to simulate new UAT data
current_data = reference_data.copy()
current_data["salary"] = current_data["salary"] * 1.5

# Generate a data drift report
report = Report(metrics=[DataDriftPreset()])

result = report.run(
    reference_data=reference_data,
    current_data=current_data
)

# Save the report as an HTML file
result.save_html("evidently_report.html")

print("Evidently monitoring completed successfully!")
print("Report saved as evidently_report.html")
