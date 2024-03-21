
import csv
import pygsheets
# google-api-python-client google-auth pygsheets

gc = pygsheets.authorize(service_file='my_creds.json')

spreadsheet = gc.open_by_key('YOUR_SHEET_ID_HERE')

# ---Open the first worksheet in the spreadsheet 
worksheet = spreadsheet.sheet1

#--  Path to the CSV file
csv_file_path = 'reviews.csv'

# -- Read data from CSV file
rows = []
with open(csv_file_path, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        rows.append(row)

# Update Google Sheets
worksheet.update_values('A1', rows)

print('Data successfully updated to Google Sheets.')
