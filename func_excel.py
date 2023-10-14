import openpyxl
from tkinter import Tk, filedialog
from func_update_table import read_data



def excel(file_name):
    headers = ["Tarih", "Lokasyon", "İrsaliye No", "Önceki Miktar", "İşlem", "Sonraki Miktar"]
    names_dict = read_data(file_name)

    workbook = openpyxl.Workbook()

    for item in names_dict.keys():

        sheet = workbook.create_sheet(title=item)
        sheet.append(headers)
        
        data = names_dict[item]
        for row in data:
            sheet.append(row)

    
    # Create a Tkinter root window
    root = Tk()
    root.withdraw()  # Hide the root window

    # Ask the user to choose a directory and filename for saving
    file_path = filedialog.asksaveasfilename(defaultextension='.xlsx', filetypes=[('Excel Files', '*.xlsx')])

    if file_path:
        # Save the Excel file
        workbook.save(file_path)
        print(f"File saved to: {file_path}")
    else:
        print("Save operation cancelled.")

    # Close the Tkinter root window
    root.destroy()

    


    





