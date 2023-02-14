import requests
import json          # Must import modules, may the force be with you
import pandas as pd
import smtplib
from email.mime.text import MIMEText

# You must Set up Sonar API credentials and URL
sonar_url = "https://api.sonar.example.com"
sonar_api_key = "abc123"

# Set up email credentials
email_host = "smtp.example.com"
email_username = "automated@example.com"
email_password = "password123"

# Make API request to get data from Sonar
response = requests.get(f"{sonar_url}/data", headers={"Authorization": f"Bearer {sonar_api_key}"})
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
    message["From"] = email_username
    message["To"] = team_member

    # Send email to team member
    with smtplib.SMTP(email_host) as smtp:
        smtp.login(email_username, email_password)
        smtp.send_message(message)


# I'm using the requests module to make an API request to Sonar and retrieve data, 
# passing in the API key in the headers. We're then using the JSON module to parse the 
# data into a Python dictionary and the Pandas module to convert the data into a DataFrame. 
# Then I perform initial data processing and filtering on the data frame to isolate new items for triage. 
# Then I'm using a for loop to assign the triaged items to team members and the 
# SMTPlib module to send emails to those team members with the assigned items as HTML tables.