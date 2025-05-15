import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

def log_to_google_sheets(profit):
    try:
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('gsheets_key.json', scope)
        client = gspread.authorize(creds)
        sheet = client.open("ForexArbitrageLog").sheet1
        sheet.append_row([str(datetime.now()), round(profit, 2)])
    except Exception as e:
        print("Google Sheets Error:", e)