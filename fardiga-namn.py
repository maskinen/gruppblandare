import tkinter as tk
from tkinter import messagebox
import random

# Jag skapar huvudfönstret
root = tk.Tk()
root.title("Grupptilldelning")  # Jag sätter titeln på Tkinter-fönstret
root.geometry("400x400")  # Jag sätter fönstrets storlek

# Jag skapar en lista för att lagra namn från filen
names = []
group_size = 0  # Variabel för att lagra vald gruppstorlek

# Jag läser in namnen från "klassnamn.txt" och fyller listan
def load_names_from_file():
    try:
        with open("klassnamn.txt", "r") as file:  # Öppna filen i läsläge
            for line in file:
                names.append(line.strip())  # Lägg till varje namn i listan
        update_name_list()  # Uppdatera listboxen med namnen
    except FileNotFoundError:
        messagebox.showwarning("Fel", "Filen klassnamn.txt hittades inte")

# Den här funktionen uppdaterar listan med namn som visas i Tkinter
def update_name_list():
    name_listbox.delete(0, tk.END)  # Jag rensar den visade listan först
    for name in names:  # Jag lägger till alla namn från names-listan
        name_listbox.insert(tk.END, name)  # Jag sätter in namnet i listboxen

# Jag skapar en funktion för att ta bort ett valt namn från listan
def remove_name():
    selected_name = name_listbox.get(tk.ACTIVE)  # Jag hämtar det markerade namnet från listboxen
    if selected_name in names:  # Jag kontrollerar om namnet finns i listan
        names.remove(selected_name)  # Jag tar bort namnet från listan
        update_name_list()  # Jag uppdaterar listan som visas
    else:
        messagebox.showwarning("Varning", "Namn ej hittat")

# Jag skapar en funktion för att välja och sätta gruppstorlek
def choose_group_size():
    global group_size  # Jag använder en global variabel för gruppstorlek
    try:
        size = int(group_size_entry.get())  # Jag försöker omvandla textfältets värde till ett heltal
        if size > 0:  # Jag kontrollerar att gruppstorleken är större än noll
            group_size = size  # Jag sätter gruppstorleken
            messagebox.showinfo("Info", f"Gruppstorlek satt till: {group_size}")  # Jag visar ett meddelande
        else:
            messagebox.showwarning("Varning", "Ogiltig gruppstorlek")  # Jag visar en varning om storleken är ogiltig
    except ValueError:
        messagebox.showwarning("Varning", "Ange ett giltigt tal")  # Jag visar en varning om användaren inte matat in ett tal

# Jag skapar en funktion för att skapa slumpmässiga grupper baserat på inmatade namn
def create_groups():
    if group_size <= 0:  # Jag kontrollerar att gruppstorlek har valts
        messagebox.showwarning("Varning", "Ange en giltig gruppstorlek först!")
        return
    if len(names) == 0:  # Jag kontrollerar att det finns minst ett namn i listan
        messagebox.showwarning("Varning", "Det finns inga namn att skapa grupper med!")
        return

    random.shuffle(names)  # Jag slumpar ordningen på namnlistan
    # Jag delar upp namnen i grupper baserat på den valda gruppstorleken
    groups = [names[i:i + group_size] for i in range(0, len(names), group_size)]

    result = ""  # Jag skapar en string för att lagra resultatet av gruppindelningen
    for idx, group in enumerate(groups):
        result += f"Grupp {idx + 1}: {', '.join(group)}\n"  # Jag skapar gruppindelning i textform

    messagebox.showinfo("Grupper skapade", result)  # Jag visar grupperna i en popup

# Jag skapar widgetar (knappar, listbox) för visning och borttagning av namn
name_listbox = tk.Listbox(root)
name_listbox.pack(pady=5)

# Jag skapar en knapp för att ta bort det valda namnet från listan
tk.Button(root, text="Ta bort valt namn", command=remove_name).pack(pady=5)

# Jag skapar ett fält för gruppstorlek och en etikett
group_size_label = tk.Label(root, text="Gruppstorlek:")  # Jag lägger till en etikett för gruppstorleksinmatning
group_size_label.pack(pady=5)

group_size_entry = tk.Entry(root)  # Jag skapar ett textfält för att mata in gruppstorlek
group_size_entry.pack(pady=5)

# Jag skapar en knapp för att bekräfta och välja gruppstorlek
tk.Button(root, text="Välj gruppstorlek", command=choose_group_size).pack(pady=5)

# Jag skapar en knapp för att skapa slumpmässiga grupper
tk.Button(root, text="Skapa grupper", command=create_groups).pack(pady=5)

# Jag skapar en knapp för att avsluta programmet
tk.Button(root, text="Avsluta", command=root.quit).pack(pady=5)

# Jag laddar in namnen från filen när programmet startar
load_names_from_file()

# Jag startar Tkinter-huvudloopen (för att visa fönstret)
root.mainloop()