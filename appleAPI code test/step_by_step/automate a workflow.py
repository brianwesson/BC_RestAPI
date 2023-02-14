import requests
import json
import pandas as pd
import smtplib
from email.mime.text import MIMEText

# Set up Sonar API credentials
sonar_url = "https://api.sonar.example.com"
sonar_username = "<your_username>"
sonar_password = "<your_password>"

# Make API request to get data from Sonar
response = requests.get(f"{sonar_url}/data", auth=(sonar_username, sonar_password))
data = json.loads(response.text)

# Parse data into a pandas DataFrame
df = pd.json_normalize(data)

# Do initial data processing and filtering
filtered_data = df[df["status"] == "new"]

# Triage and assign to team members
for team_member in ["alice@example.com", "bob@example.com", "charlie@example.com"]:
    assigned_data = filtered_data[filtered_data["assignee"] == team_member]

    if assigned_data.empty:
        continue

    # Format assigned data as an email message
    message = MIMEText(assigned_data.to_html(), "html")
    message["Subject"] = f"Sonar data assigned to {team_member}"
    message["From"] = "automated@example.com"
    message["To"] = team_member

    # Send email to team member
    with smtplib.SMTP("smtp.example.com") as smtp:
        smtp.send_message(message)
