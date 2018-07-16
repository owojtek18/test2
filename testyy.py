# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive
#
# #1st authentification
# gauth = GoogleAuth()
# gauth.LocalWebserverAuth() # Creates local webserver and auto handles
# #authentication.
# drive = GoogleDrive(gauth)
#
# # file1 = drive.CreateFile()
# # file1.SetContentFile(r'C:\Users\wojci\Desktop\test\Surgeries_TEMAPLATES.xls')
# # file1.Upload()
#
# file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
# for file1 in file_list:
#   print('title: %s, id: %s' % (file1['title'], file1['id']))

from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# Setup the Sheets API
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secrets.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('sheets', 'v4', http=creds.authorize(Http()))

# Call the Sheets API
SPREADSHEET_ID = '1BUFt3rDrg4tuS7yTrYlMhm-pfqTdKHTSHAv9iWCpy9I'
RANGE_NAME = 'A2:B12'
result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                             range=RANGE_NAME).execute()
values = result.get('values', [])
print(values)
if not values:
    print('No data found.')
else:
    print('Name, Major:')
    for row in values:
        # Print columns A and E, which correspond to indices 0 and 4.
        print('%s, %s' % (row[0], row[1]))