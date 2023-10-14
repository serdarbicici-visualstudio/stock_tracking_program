from func_update_table import read_data

#"Tarih", "Lokasyon", "İrsaliye No", "Önceki Miktar", "İşlem", "Sonraki Miktar"

def submit(namebox, stockbox, combobox_name, unit, file_name):
    
    # Retrieve user inputs from entry fields

    try:
        name = namebox.get()
        stock = stockbox.get()
        stock = float(stock)
    except ValueError:
        return

    if unit == "":
        return



    data = [["Başlangıç Stoğu","","",stock,stock,stock]]

    with open(file_name, "a") as file:
        
        file.write(str(name))
        file.write("-")
        file.write(unit)
        file.write("=")
        file.write(str(data))
        file.write("\n")

    names = read_data(file_name)
    names = [i for i in names]
    combobox_name.configure(values=names)
