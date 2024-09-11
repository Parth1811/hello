import json
import os
import re
from datetime import datetime

import gspread
import requests
from oauth2client.service_account import ServiceAccountCredentials

AUTOMATION_SHEET_ID = 1
SEASONS = ["Winter 2024", "Spring 2025", "Summer 2025"]

# Setup google credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(os.path.expanduser("~/google_credentials.json"), scope)
client = gspread.authorize(creds)

spreadsheet = client.open("Parth 2025 Applications")
sheet = spreadsheet.get_worksheet(AUTOMATION_SHEET_ID)
assert sheet.title == "Automation"


def sanitize_title(title):
    title = title.lower()
    title = re.sub(r'summer|winter|spring|2024|2025', '', title)
    title = re.sub(r'\s+', ' ', title)
    return title.strip().title()

def get_season(title):
    if "summer" in title:
        return SEASONS[2]
    if "spring" in title:
        return SEASONS[1]
    if "winter" in title:
        return SEASONS[0]
    else:
        return SEASONS[2]


req = requests.get("https://raw.githubusercontent.com/Ouckah/Summer2025-Internships/dev/.github/scripts/listings.json")
if req.status_code == 200:
    listings = json.loads(req.text)

    # Listings have the following keys:
    #  'date_updated', 'url', 'locations', 'sponsorship', 'active', 'company_name', 
    # 'title', 'season', 'source', 'id', 'date_posted', 'company_url', 'is_visible'

    sorted_listings = sorted(listings, key=lambda x: x["date_updated"])
    header = ["Title", "Posted on", "Deadline", "Company", "Location(s)", "Season", "Status", "ID"]
    rows = [header]
    for listing in listings:        
        row = [
            f'=HYPERLINK("{listing["url"]}", "{sanitize_title(listing["title"])}")',
            datetime.fromtimestamp(listing["date_posted"]).strftime("%d, %b %y"),
            "",
            listing["company_name"],
            ", ".join(listing["locations"]),
            get_season(listing["title"]),
            "",
            listing["id"],
        ]

        rows.append(row)

    sheet.clear()
    sheet.update(rows, value_input_option='USER_ENTERED')
