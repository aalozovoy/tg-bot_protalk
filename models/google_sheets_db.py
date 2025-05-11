from google.oauth2 import service_account
import gspread
from config.settings import Config


class GoogleSheetsDB:
    """Работа с Google Sheets как БД (пример из статьи)."""

    def __init__(self):
        self.creds = service_account.Credentials.from_service_account_info(
            Config.GOOGLE_CREDENTIALS
        )
        self.client = gspread.authorize(self.creds)

    def save_procurement_data(self, data: dict):
        sheet = self.client.open_by_key(Config.GOOGLE_SHEETS_ID).sheet1
        sheet.append_row([data["product"], data["kved"], data["status"]])