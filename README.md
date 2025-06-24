# SAP to Power BI Automated Reporting

## Overview

This project automates the entire workflow of extracting business data from SAP, transforming it, and generating dynamic reports in Power BI. By leveraging Python automation, CLI tools, and Power BI APIs, the solution eliminates manual effort, ensures timely updates, and delivers accurate, data-driven insights.

---

## Features

- **Automated SAP Data Extraction:**  
  Uses Python (`pyautogui`) to interact with the SAP GUI and export required data as an Excel file.
- **Seamless Data Integration:**  
  The exported Excel file is directly used as a data source for Power BI reports.
- **Automated Power BI Refresh:**  
  Utilizes tools like `pbi-tools` (for Power BI Desktop) or Power BI REST API (for Power BI Service) to refresh reports automatically.
- **Optional Report Export/Distribution:**  
  Refreshed reports can be exported as PDF or other formats and distributed via email.
- **Scheduled Execution:**  
  The workflow can be run periodically using schedulers like Windows Task Scheduler or cron.

---

## Workflow
![image](https://github.com/user-attachments/assets/c6de4cf8-096f-40aa-ae94-48972760b141)


## Technologies Used

- **Python** (`pyautogui`, `subprocess`, `requests`, `msal`)
- **Power BI Desktop** and/or **Power BI Service**
- **pbi-tools** (CLI automation for Power BI Desktop)
- **Task Scheduler / Cron** (for automation scheduling)
- **SAP GUI**

---

## Usage

### 1. SAP Data Extraction

Automate SAP GUI to export data:

```python
import pyautogui
# Your SAP automation logic here to export and save as sap.xlsx
```

### 2. Power BI Report Refresh

**For Power BI Desktop:**

Install [pbi-tools](https://github.com/pbi-tools/pbi-tools):

```sh
dotnet tool install --global pbi-tools
```

Refresh your PBIX file using the latest Excel data:

```sh
pbi-tools refresh --file "C:\Path\To\YourReport.pbix"
```

**For Power BI Service:**

Use Python with `requests` and `msal` to trigger a dataset refresh:

```python
import requests
from msal import ConfidentialClientApplication

# Set up your Azure AD and Power BI workspace info
TENANT_ID = 'YOUR_TENANT_ID'
CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
WORKSPACE_ID = 'YOUR_WORKSPACE_ID'
DATASET_ID = 'YOUR_DATASET_ID'

authority_url = f"https://login.microsoftonline.com/{TENANT_ID}"
scope = ["https://analysis.windows.net/powerbi/api/.default"]

app = ConfidentialClientApplication(
    CLIENT_ID, authority=authority_url, client_credential=CLIENT_SECRET
)
token_response = app.acquire_token_for_client(scopes=scope)
access_token = token_response['access_token']

refresh_url = f"https://api.powerbi.com/v1.0/myorg/groups/{WORKSPACE_ID}/datasets/{DATASET_ID}/refreshes"
headers = {'Authorization': f'Bearer {access_token}'}
response = requests.post(refresh_url, headers=headers)

print(response.status_code, response.text)
```

---

## Scheduling the Workflow

- Use **Windows Task Scheduler** or **cron** to schedule the combined scripts for periodic, unattended execution.

---

## Customization

- Adjust the SAP automation logic to match your organization's SAP GUI flow.
- Update file paths and Power BI configuration as needed.
- Extend with report export and email distribution if desired.

---

## Benefits

- Reduces manual reporting workload.
- Ensures up-to-date, consistent reporting.
- Enables timely business insights.

---

## Contact

For questions, feedback, or collaboration:

- **Email:** sujanlankeppanavar5@gmail.com
- **LinkedIn:** [Your LinkedIn](https://www.linkedin.com/in/sujan-lankeppanavar-45930a2a3/)
