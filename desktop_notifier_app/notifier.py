from plyer import notification
import tkinter as tk
from tkinter import simpledialog, messagebox
import schedule
import threading
import time

def show_notification(notification_text, custom_title, custom_message):
    notification.notify(
        title=custom_title,
        message=custom_message,
        app_name="Desktop Notifier",
    )

def schedule_notification():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    notification_text = simpledialog.askstring("Notification", "Enter Notification:")
    if notification_text:
        custom_title = simpledialog.askstring("Custom Title", "Enter Custom Title:")
        custom_message = simpledialog.askstring("Custom Message", "Enter Custom Message:")
        schedule_time = simpledialog.askstring("Schedule", "Enter Schedule (HH:MM):")
        if schedule_time:
            try:
                hh, mm = map(int, schedule_time.split(':'))
                current_time = time.localtime()
                if current_time.tm_hour < hh or (current_time.tm_hour == hh and current_time.tm_min <= mm):
                    schedule.every().day.at(f"{hh:02}:{mm:02}").do(
                        show_notification, notification_text, custom_title, custom_message)
                    messagebox.showinfo("Scheduled", f"Notification scheduled for {schedule_time}")
                else:
                    messagebox.showerror("Error", "Invalid time. Please select a future time.")
            except ValueError:
                messagebox.showerror("Error", "Invalid time format. Please use HH:MM format.")
        else:
            messagebox.showerror("Error", "Please enter a schedule time.")
    else:
        messagebox.showerror("Error", "Please enter a notification text.")

def run_notifier():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    threading.Thread(target=run_notifier).start()
    schedule.every().day.at("00:00").do(lambda: None)  # Start the scheduling loop
    tk.Tk().withdraw()  # Hide the main window
    schedule_notification()
