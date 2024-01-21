import tkinter as tk
from datetime import datetime
import pytz

def update_time():

    timezone_aest = pytz.timezone('Australia/Sydney')
    timezone_cet = pytz.timezone('Europe/Berlin')

    time_aest = datetime.now(timezone_aest).strftime('%H:%M:%S')
    time_cet = datetime.now(timezone_cet).strftime('%H:%M:%S')

    date_now = datetime.now(timezone_aest).strftime('%Y-%m-%d')

    label_time_aest.config(text=time_aest)
    label_time_cet.config(text=time_cet)
    label_date.config(text=date_now)

    root.after(1000, update_time)

root = tk.Tk()
root.title("Time Display")
root.geometry("400x400")

canvas = tk.Canvas(root, width=200, height=200, highlightthickness=2, highlightbackground="black")
canvas.pack(expand=True)

label_info = tk.Label(canvas, text="The time in:", font=('Arial', 10))
canvas.create_window(100, 20, window=label_info)

label_aest = tk.Label(canvas, text="AEST", font=('Arial Black', 12))
label_time_aest = tk.Label(canvas, font=('Arial', 10))
canvas.create_window(100, 50, window=label_aest)
canvas.create_window(100, 70, window=label_time_aest)

label_cet = tk.Label(canvas, text="CET", font=('Arial Black', 12))
label_time_cet = tk.Label(canvas, font=('Arial', 10))
canvas.create_window(100, 100, window=label_cet)
canvas.create_window(100, 120, window=label_time_cet)

label_date = tk.Label(canvas, font=('Arial', 10))
canvas.create_window(100, 150, window=label_date)

update_time()
root.mainloop()
