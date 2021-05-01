import bs4
import os

with open(os.path.expanduser('~/Desktop/Placements, IIT Bombay.html'), 'r') as f:
    webpage = f.read()

print('Extracting the Jafs from the html file...........')
soup = bs4.BeautifulSoup(webpage, "html.parser")
a = soup.find_all("tr", {"class": "mat-row cdk-row ng-star-inserted"})
jafs = []

for row in a:
    cells =  row.findChildren("td")
    name = cells[0].contents[0]
    jaf = cells[1].contents[0]
    role = cells[2].findChild('a').contents[0]
    href = cells[2].findChild('a').attrs['href']
    jafs.append([name, jaf, role, href])
    # print("%s,%s,%s,%s" % (name, jaf, role, href))

jafs.sort()
# print(jafs)

# from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1CLTM6d2Q8-MI5QuapXyA3zc9fGi09pXOA7JXSTltSbU'
SAMPLE_RANGE_NAME = 'Sheet1!A1:D'
SAMPLE_RANGE_NAME1 = 'Sheet1!D1:D'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()

    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME1).execute()
    values = result.get('values')
    values = [x[0] for x in values]
    new = []
    if len(jafs) != len(values):
        for jaf in jafs:
            if jaf[3] in values:
                continue
            new.append(jaf)

    batch_update_values_request_body = {
        'value_input_option': '2',
        'data': [{
            "range": "Sheet1!A%d:D%d" %(len(values)+1, len(jafs)+1),
            "values": new
        }],
    }

    sort_filter = {
        "requests": [
            {
            "sortRange": {
                "range": {
                "sheetId": 0,
                "startRowIndex": 0,
                "endRowIndex": len(jafs),
                "startColumnIndex": 0,
                "endColumnIndex": 4
                },
                "sortSpecs": [
                {
                    "dimensionIndex": 0,
                    "sortOrder": "ASCENDING"
                }
                ]
            }
            }
        ]
    }


    if len(new) != 0:
        request = service.spreadsheets().values().batchUpdate(spreadsheetId=SAMPLE_SPREADSHEET_ID, body=batch_update_values_request_body)
        response = request.execute()
        for jaf in new:
            print("Added " + jaf[0])
    else:
        print("Nothing to update")

    print("Sorrting the new jAFS.........")
    request = service.spreadsheets().batchUpdate(spreadsheetId=SAMPLE_SPREADSHEET_ID, body=sort_filter)
    response = request.execute()

    return service

if __name__ == '__main__':
    service = main()



