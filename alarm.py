from datetime import datetime
import time
import tkinter as tk
from tkinter import messagebox
import threading

def trigger_alarm():
  
    for _ in range(5):
        root.bell()
        time.sleep(0.5)

def check_alarm(alarm_time_str):
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time_str:
            
            threading.Thread(target=trigger_alarm, daemon=True).start()
            messagebox.showinfo("Alarm", " Wake Up! Time's up!")
            break
        time.sleep(1)

def set_alarm():
    alarm_time = f"{hour_var.get()}:{minute_var.get()}:{second_var.get()}"
    messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")
    threading.Thread(target=check_alarm, args=(alarm_time,), daemon=True).start()


root = tk.Tk()
root.title("Simple Alarm Clock")
root.geometry("350x200")
root.config(bg="#f4f4f9")

tk.Label(root, text="Set Alarm Time (24-Hour)", font=("Arial", 14, "bold"), bg="#f4f4f9").pack(pady=10)

frame = tk.Frame(root, bg="#f4f4f9")
frame.pack()

hour_var = tk.StringVar(value="00")
minute_var = tk.StringVar(value="00")
second_var = tk.StringVar(value="00")


tk.Entry(frame, textvariable=hour_var, width=3, font=("Arial", 16)).pack(side=tk.LEFT, padx=5)
tk.Label(frame, text=":", font=("Arial", 16), bg="#f4f4f9").pack(side=tk.LEFT)
tk.Entry(frame, textvariable=minute_var, width=3, font=("Arial", 16)).pack(side=tk.LEFT, padx=5)
tk.Label(frame, text=":", font=("Arial", 16), bg="#f4f4f9").pack(side=tk.LEFT)
tk.Entry(frame, textvariable=second_var, width=3, font=("Arial", 16)).pack(side=tk.LEFT, padx=5)

set_btn = tk.Button(root, text="Set Alarm", command=set_alarm, bg="#007BFF", fg="white", font=("Arial", 12), width=15)
set_btn.pack(pady=20)

root.mainloop()