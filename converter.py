import datetime
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from Birthday import BirthdayEvent, BirthdayCollection
import os

SCOPES = ["https://www.googleapis.com/auth/calendar.events"]
CLIENT_SECRET_FILE = 'credentials.json'
API_KEY = os.environ.get('API_KEY','')

def main():
    """Create birthday events"""

    birthdays = BirthdayCollection()
    birthdays.load_birthdays()
    birthdays.list_birthdays()

    if not os.path.exists('token.json'):
        raise Exception("No token file provided piece of shit")

    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_FILE, SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar','v3', credentials=creds, developerKey=API_KEY)

        for birthday in birthdays:
            event = {
                'summary': f"{birthday.name}'s Birthday",
                'description':birthday.name,
                'start':{
                    'date':datetime.datetime.strftime(birthday.date,'%Y-%m-%d'),
                    'timeZone':'Asia/Singapore'
                },
                'end':{
                    'date':datetime.datetime.strftime(birthday.end_date,'%Y-%m-%d'),
                    'timeZone':'Asia/Singapore'
                },
                'recurrence':[
                    'RRULE:FREQ=YEARLY'
                ]
            }

            event = service.events().insert(calendarId='primary', body=event).execute()
            print(f'Event created: %s' % (event.get('htmlLink')))

    except HttpError as error:
        print(f'An error occurred :{error}')

if __name__ == '__main__':
    main()

