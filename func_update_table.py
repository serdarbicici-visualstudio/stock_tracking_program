
names = dict()

def read_data(file_name):
    with open(file_name, "r") as file:
        for line in file:
            name, data = line.strip().split("=")
            data = eval(data)
            
            names[name] = data

    return names


def update_table(selection, table, label_name, file_name):

    names = read_data(file_name)
    stock = names[selection]
    s = 0
    for i in stock:
        s = s + float(i[-2])

    name_and_unit = selection.split("-")


    label_name.configure(text=str(s)+" "+name_and_unit[-1])

    table.delete(*table.get_children())  # Clear existing rows
    
    for i in names:
        
        if i == selection:
            d = names[i]
            
            for x in range(len(d)):    
                
                dt = d[x]
                
                date = dt[0]
                location = dt[1]
                number = dt[2]
                pre = dt[3]
                eff = dt[4]
                after = dt[5]

                if float(eff) < 0:
                    table.insert('', 'end', values=(date, location, number, pre, eff, after), tags="negative")
                
                else: 
                    table.insert('', 'end', values=(date, location, number, pre, eff, after), tags="positive")
  