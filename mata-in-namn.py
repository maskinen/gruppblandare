import tkinter as tk
from tkinter import messagebox
import random

# Skapar huvudfönstret
root = tk.Tk()
root.title("Grupptilldelning för DOE24")  # Sätter titeln på Tkinter-fönstret
root.geometry("400x400")  # Sätter fönstrets storlek

# Lista för att lagra namnen i klassen
names = []  # En tom lista som kommer att fyllas med namn
group_size = 0  # Variabel för att lagra vald gruppstorlek

# Funktion för att kunna uppdatera listan med namn som visas i Tkinter
def update_name_list():
    name_listbox.delete(0, tk.END)  # Rensar den visade listan först
    for name in names:  # Lägger till alla namn från names-listan
        name_listbox.insert(tk.END, name)  # Sätter in namnet i listboxen

# Funktion för att lägga till namnen i listan
def add_name():
    name = name_entry.get()  # Hämtar inmatat namnen från textfältet
    if name:  # Kontrollerar om namnet inte är tomt
        names.append(name)  # Lägger till namnet i listan
        name_entry.delete(0, tk.END)  # Rensar textfältet efter inmatning
        update_name_list()  # Uppdaterar listan som visas
    else:
        messagebox.showwarning("Varning", "Ange ett namn.")  # Varning om textfältet är tomt

# Funktion för att ta bort ett valt namn från listan
def remove_name():
    selected_name = name_listbox.get(tk.ACTIVE)  # Hämtar det markerade namnet från listboxen
    if selected_name in names:  # Kontrollera om namnet finns i listan
        names.remove(selected_name)  # Tar bort namnet från listan
        update_name_list()  # Uppdaterar listan som visas
    else:
        messagebox.showwarning("Varning", "Namn ej hittat")  # Varning om namnet inte finns

# Funktion för att välja och sätta gruppstorlek
def choose_group_size():
    global group_size  # Använder global variabel för gruppstorlek
    try:
        size = int(group_size_entry.get())  # Försöker omvandla textfältets värde till ett heltal
        if size > 0:  # Kontrollerar att gruppstorleken är större än noll
            group_size = size  # Sätter gruppstorleken
            messagebox.showinfo("Info", f"Gruppstorlek satt till: {group_size}")  # Visar meddelande
        else:
            messagebox.showwarning("Varning", "Ogiltig gruppstorlek")  # Varning om storleken är ogiltig
    except ValueError:
        messagebox.showwarning("Varning", "Ange ett giltigt tal")  # Varning om användaren inte matat in ett tal

# Funktion för att skapa slumpmässiga grupper baserat på inmatade namn
def create_groups():
    if group_size <= 0:  # Kontrollera att gruppstorlek har valts
        messagebox.showwarning("Varning", "Ange en giltig gruppstorlek först!")
        return
    if len(names) == 0:  # Kontrollera att det finns minst ett namn i listan
        messagebox.showwarning("Varning", "Lägg till minst ett namn!")
        return

    random.shuffle(names)  # Slumpa ordningen på namnlistan
    # Dela upp namnen i grupper baserat på den valda gruppstorleken
    groups = [names[i:i + group_size] for i in range(0, len(names), group_size)]

    result = ""  # String för att lagra resultatet av gruppindelningen
    for idx, group in enumerate(groups):
        result += f"Grupp {idx + 1}: {', '.join(group)}\n"  # Skapa gruppindelning i textform

    messagebox.showinfo("Grupper skapade", result)  # Visa grupperna i en popup

# Skapa widgetar (textfält, knappar, listbox) för inmatning och visning av namn
name_entry = tk.Entry(root)  # Textfält för att mata in namn
name_entry.pack(pady=5)

# Knapp för att lägga till namn till listan
tk.Button(root, text="Lägg till namn", command=add_name).pack(pady=5)

# Listbox för att visa namnen som lagts till
name_listbox = tk.Listbox(root)
name_listbox.pack(pady=5)

# Knapp för att ta bort det valda namnet från listan
tk.Button(root, text="Ta bort valt namn", command=remove_name).pack(pady=5)

# Gruppstorleksfält och etikett
group_size_label = tk.Label(root, text="Gruppstorlek:")  # Etikett för gruppstorleksinmatning
group_size_label.pack(pady=5)

group_size_entry = tk.Entry(root)  # Textfält för att mata in gruppstorlek
group_size_entry.pack(pady=5)

# Knapp för att bekräfta och välja gruppstorlek
tk.Button(root, text="Välj gruppstorlek", command=choose_group_size).pack(pady=5)

# Knapp för att skapa slumpmässiga grupper
tk.Button(root, text="Skapa grupper", command=create_groups).pack(pady=5)

# Knapp för att avsluta programmet
tk.Button(root, text="Avsluta", command=root.quit).pack(pady=5)

# Starta Tkinter-huvudloopen (för att visa fönstret)
root.mainloop()