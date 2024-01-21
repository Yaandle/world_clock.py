import tkinter as tk
from datetime import datetime
import pytz
from tkinter.font import Font

def update_time():
    aest = pytz.timezone('Australia/Sydney')
    cet = pytz.timezone('Europe/Berlin')
    time_aest = datetime.now(aest).strftime('%H:%M:%S')
    time_cet = datetime.now(cet).strftime('%H:%M:%S')
    date = datetime.now(aest).strftime('%Y-%m-%d')  # Use AEST for the date
    label_time.config(text=f"The time in:\nAEST {time_aest}\nCET {time_cet}")
    label_date.config(text=date)
    root.after(1000, update_time)

root = tk.Tk()
root.title("Timezone Display")
root.geometry('400x400')
root.resizable(False, False)

font_label = Font(family="Arial Black", size=12)

label_time = tk.Label(root, font=font_label, justify=tk.CENTER)
label_date = tk.Label(root, font=font_label, justify=tk.CENTER)

label_time.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
label_date.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

update_time()
root.mainloop()
