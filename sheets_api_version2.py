import gspread
from oauth2client.service_account import ServiceAccountCredentials
from apiclient import discovery


SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://spreadsheets.google.com/feeds"]
CREDS = "creds_bunko.json"
# gc = gspread.service_account()

class SheetsAPI:
    sheet = None

    @classmethod
    def init_sheet(cls):
        creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS, SCOPES)
        cls = gspread.authorize(creds)
        # service = discovery.build("sheets", "v4", credentials=creds)
        # cls.sheet = service.spreadsheets()
    
    @classmethod
    def get_sheet_data(cls, sheet_id, sheet_range):
        if cls.sheet == None:
            cls.init_sheet()
        
        sheet_opened = gspread.service_account().open_by_key(sheet_id) # opens a sheet using passed in ID
        worksheet_opened = sheet_opened.get_worksheet(0)
        values_list = worksheet_opened.col_values(1)
    
    # @classmethod
    # def append_to_sheet(cls, sheet_id, sheet_range, value):
    #     if cls.sheet == None:
    #         cls.init_sheet()
        
    #     value_input_option = "USER_ENTERED"
        
    #     insert_data_option = "INSERT_ROWS"
        
    #     value_input_body = {
    #         "majorDimension" : "ROWS"
    #         "values" : [[value]]
    #         }
        
    #     request = cls.sheet.values.append(spreadsheetId = sheet_id, range = sheet_range, valueInputOption = value_input_option, insertDataOption = insert_data_option, body = value_input_body)
    #     response = request.execute()

    #     return response
#         client = gspread.authorize(creds)
# sheet_id = ""

# sheet = client.open_by_key(sheet_id)
# value_list= sheet.sheet1.row_values(1)
# print(value_list)