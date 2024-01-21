import tkinter as tk
from datetime import datetime
import pytz

def update_time():
    timezone_aest = pytz.timezone('Australia/Sydney')
    timezone_cet = pytz.timezone('Europe/Berlin')
    time_aest = datetime.now(timezone_aest).strftime('%H:%M:%S')
    time_cet = datetime.now(timezone_cet).strftime('%H:%M:%S')
    date_now = datetime.now(timezone_aest).strftime('%Y-%m-%d')
    label_time_in_aest.config(text="The time in ")
    label_time_aest.config(text="AEST: " + time_aest)
    label_time_in_cet.config(text="The time in ")
    label_time_cet.config(text="CET: " + time_cet)
    label_date.config(text=date_now)
    root.after(1000, update_time)

root = tk.Tk()
root.title("Time Display")
root.geometry("400x400")

canvas = tk.Canvas(root, width=400, height=400, highlightthickness=2, highlightbackground="black")
canvas.pack(expand=True)

label_time_in_aest = tk.Label(canvas, font=('Arial', 13))
label_time_aest = tk.Label(canvas, font=('Arial Black', 16))
label_time_in_cet = tk.Label(canvas, font=('Arial', 13))
label_time_cet = tk.Label(canvas, font=('Arial Black', 16))
label_date = tk.Label(canvas, font=('Arial', 10))

label_time_in_aest.place(x=200, y=120, anchor="center")
label_time_aest.place(x=200, y=150, anchor="center")
label_time_in_cet.place(x=200, y=180, anchor="center")
label_time_cet.place(x=200, y=210, anchor="center")
label_date.place(x=200, y=250, anchor="center")

update_time()
root.mainloop()
