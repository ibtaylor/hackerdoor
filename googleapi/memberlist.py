from __future__ import print_function
import httplib2

from apiclient import discovery
from oauth2client import client
from oauth2client.file import Storage

from oauth2client.service_account import ServiceAccountCredentials

from pprint import pprint

### Created from the sample Google Sheet API tutorial.
def main():
    
    scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    # Use the Hackerdoor Service Account
    credentials = ServiceAccountCredentials.from_json_keyfile_name('./configs/hackerdoor-servicecredentials.json', scopes)
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http ,
        discoveryServiceUrl=discoveryUrl)

    # The Memberlist Google Doc
    spreadsheetId = '1sakXpA_H5vs3_addWkrPbccDVcoxFx13yDpudYlqInM'

    rangeName = 'HackerdoorView!A2:E'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        # Dec is the decimal equivalent of FC+CC
        # With Google Sheets, if a cell is empty, no data is returned for that column
        # So the row object may contain between 1 and 5 columns, we'll have to deal with None's.
        print('Name, Status, Card FC, Card CC, Card Dec:')
        for row in values:
            pprint(row)
            

if __name__ == '__main__':
    main()