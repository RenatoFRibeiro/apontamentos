def read_xml(file_path, sheet_name, column_indices):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb[sheet_name]
    
    data_rows = []
    
    for row in sheet.iter_rows(min_row=2, values_only=True):  # Assuming the first row contains headers
        row_data = [row[column_index - 1] for column_index in column_indices]  # Column indices are 1-based
        data_rows.append(row_data)
        print(row_data)
        
    wb.close()
    return data_rows
