def toSpreadSheet(filtered_options):
    from oauth2client.service_account import ServiceAccountCredentials
    import gspread, time, math
    from tqdm import tqdm
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("Selling Puts ROI and Delta spreadsheet for scanner").sheet1  # Open the spreadhseet

    progress_bar = tqdm(total=len(filtered_options), disable=False)
    row = 2
    for option in filtered_options:
        cell_list = sheet.range('A{start}:P{end}'.format(start = row, end = row))
        cell_values = [str(option[0]['description']), option[1]['symbol'], option[0]['daysToExpiration'], str(option[0]['bid'] / option[0]['strikePrice']), ((option[0]['bid'] / option[0]['strikePrice']) * (365/option[0]['daysToExpiration'])), option[0]['strikePrice'], option[1]['mark'], (option[0]['strikePrice'] - option[0]['bid']), option[0]['bid'], option[0]['ask'], option[0]['delta'], option[0]['gamma'], option[0]['theta'], option[0]['rho']]
        for i, val in enumerate(cell_values):
            cell_list[i].value = val
        sheet.update_cells(cell_list)
        row += 1
        time.sleep(1)
        progress_bar.update(1)
    progress_bar.close()
