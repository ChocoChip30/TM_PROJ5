import gspread
from google.oauth2.service_account import Credentials

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("/Users/tamaramarie/Desktop/CODE/PythonProjs/ImageText/PRACTICE/credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "17pckeGtb1MvP7MAPB1IYCMxG3ayTakieiRcxgXmk8J4"
workbook = client.open_by_key(sheet_id)

# listing all worksheets
#sheets =map(lambda x : x.title,  workbook.worksheets())

#getting a particular sheet
#sheet = workbook.worksheet("Hello World!")

#changing sheet title
#sheet.update_title("Hello World!")

#update a cell
# sheet.update_acell("B3", text)
#sheet.update_cell(1, 1, "CHANGE IN TEXT")

#get value of specific cell
#value = sheet.acell("A1").value
# print(value)

# get cell by TEXT
#cell = sheet.find("FIND ME")
#print(cell.row, cell.col)

# FORMATTING CELLS
#sheet.format("A1", {"textFormat": {"bold": True}})

values = [
    ["Name", "Price", "Quantity"],
    ["Basketball", 30.45, 1],
    ["Jeans", 40.45, 2],
    ["Juice", 12.12, 5],
]

# creating new worksheet if not created already
worksheet_list = map(lambda x : x.title, workbook.worksheets())
new_worksheet_name = "Values"

if new_worksheet_name in worksheet_list:
    sheet = workbook.worksheet(new_worksheet_name)
else:
    sheet = workbook.add_worksheet(new_worksheet_name, rows = 10, cols = 10)

# clearing sheet
sheet.clear()

# updating a range of cells at a time
sheet.update(f"A1:C{len(values)}", values)

# bold titles
sheet.format("A1:C1", {"textFormat": {"bold": True}})


# adding total price and quantity
sheet.update_cell(len(values) + 1, 2, "=sum(B2:B4)")
sheet.update_cell(len(values) + 1, 3, "=sum(C2:C4)")










