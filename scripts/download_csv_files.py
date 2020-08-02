import pickle
import os.path
import csv
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/drive.readonly'] # If modifying these scopes, delete the file token.pickle
PICKLE_FILE_PATH = os.path.join(os.path.dirname(__file__), "token.pickle")
CREDENTIALS_FILE_PATH = os.path.join(os.path.dirname(__file__), "credentials.json")
SPREADSHEET_ID = "1J2Nxaoq8fk3TEQ_3n_n7SNYkQuhXLQypKims0MNazlU"
DESTINATION_DIRECTORY = os.path.join(os.getcwd(), "csv")


def main():
    print("Starting download script...")
    credentials = load_credentials()
    if not credentials or not credentials.valid:
        print("Credentials require user authentication.")
        authenticate_user(credentials)

    print("Connecting to Google Drive services...")
    service = build('sheets', 'v4', credentials=credentials)

    print("Retrieving spreadsheet with ID {} from Google Drive...".format(SPREADSHEET_ID))
    document = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()

    print("Got sheet '{}' successfully!".format(document["properties"]["title"]))
    download_sheet_tabs_to_csv_files(service, document)

    print("All CSV files updated!")


def load_credentials():
    credentials = None
    if os.path.exists(PICKLE_FILE_PATH):
        with open(PICKLE_FILE_PATH, 'rb') as token:
            credentials = pickle.load(token)
    return credentials


def authenticate_user(credentials):
    if credentials and credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE_PATH, SCOPES)
        credentials = flow.run_local_server(port=0)
    with open(PICKLE_FILE_PATH, 'wb') as token:
        pickle.dump(credentials, token)


def download_sheet_tabs_to_csv_files(service, document):
    if not os.path.isdir(DESTINATION_DIRECTORY):
        print("Directory '{}' not found, creating...", DESTINATION_DIRECTORY)
        os.mkdir(DESTINATION_DIRECTORY)
    for name, data in get_sheet_data(service, document):
        filename = os.path.join(DESTINATION_DIRECTORY, "{}.csv".format(name))
        print("\t -> Writing {} sheet to {}...".format(name, filename), end="")
        with open(filename, 'w', newline='') as fd:
            write_csv(fd, data)
        print(" Done!")


def get_sheet_data(service, document):
    sheets = [s['properties']['title'] for s in document['sheets']]
    params = {'spreadsheetId': SPREADSHEET_ID, 'ranges': sheets, 'majorDimension': 'ROWS'}
    result = service.spreadsheets().values().batchGet(**params).execute()
    for name, vr in zip(sheets, result['valueRanges']):
        yield name, vr['values']


def write_csv(file, rows):
    csv.writer(file).writerows(rows)


if __name__ == '__main__':
    main()
