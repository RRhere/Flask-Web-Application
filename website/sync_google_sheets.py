import gspread
from google.oauth2.service_account import Credentials
from .models import User

def get_google_sheet():
    # Update with the path to your service account key JSON file
    SERVICE_ACCOUNT_FILE = 'RRhere/Notes-App/notes-app.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

    credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    client = gspread.authorize(credentials)
    sheet_id="1BO2yEEIuqxL80Up81E0OtkZRsYFDDWGvsrD5qui8eCo"
    sheet = client.open_by_key(sheet_id)
    return sheet

def sync_with_google_sheets():
    sheet = get_google_sheet()

    # Fetch all users from the database
    users = User.query.all()

    # Fetch existing data to prevent duplicate headers
    existing_data = sheet.get_all_values()

    if len(existing_data) == 0:  # Add headers only if the sheet is empty
        sheet.append_row(["ID", "Email", "First Name", "Last Name", "Is Verified"])

    # Collect all user data in a list for batch update
    user_data = []
    for user in users:
        user_data.append([user.id, user.email, user.first_name, user.last_name, user.is_verified])

    # Append data in batch (for efficiency)
    sheet.append_rows(user_data)
