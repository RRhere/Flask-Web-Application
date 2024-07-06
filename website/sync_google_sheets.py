import gspread
from google.oauth2.service_account import Credentials
from .models import User

def get_google_sheet():
    # Update with the path to your service account key JSON file
    SERVICE_ACCOUNT_FILE = 'RRhere/Notes-App/website/notes-app.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

    credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    client = gspread.authorize(credentials)
    # Replace 'Your Google Sheet Name' with the name or URL of your Google Sheet
    sheet = client.open("Notes-App").sheet1
    return sheet

def sync_with_google_sheets():
    sheet = get_google_sheet()

    # Fetch all users from the database
    users = User.query.all()

    # Clear the existing data in the sheet
    sheet.clear()

    # Set the headers
    sheet.append_row(["ID", "Email", "First Name", "Last Name", "Is Verified"])

    # Append user data
    for user in users:
        sheet.append_row([user.id, user.email, user.first_name, user.last_name, user.is_verified])
