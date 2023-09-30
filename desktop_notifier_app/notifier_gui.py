import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from datetime import datetime
import schedule
import threading
from plyer import notification

class NotifierGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Desktop Notifier")

        self.label = tk.Label(root, text="Enter Notification:")
        self.label.pack()

        self.notification_text = tk.Entry(root, width=50)
        self.notification_text.pack()

        self.title_label = tk.Label(root, text="Custom Title:")
        self.title_label.pack()
        self.title_text = tk.Entry(root, width=50)
        self.title_text.pack()

        self.message_label = tk.Label(root, text="Custom Message:")
        self.message_label.pack()
        self.message_text = tk.Entry(root, width=50)
        self.message_text.pack()

        self.schedule_label = tk.Label(root, text="Schedule (HH:MM):")
        self.schedule_label.pack()
        self.schedule_text = tk.Entry(root, width=50)
        self.schedule_text.pack()

        self.notification_button = tk.Button(root, text="Schedule Notification", command=self.schedule_notification)
        self.notification_button.pack()

    def show_notification(self, notification_text, custom_title, custom_message):
        notification.notify(
            title=custom_title,
            message=custom_message,
            app_name="Desktop Notifier",
        )

    def schedule_notification(self):
        notification_text = self.notification_text.get()
        custom_title = self.title_text.get()
        custom_message = self.message_text.get()
        schedule_text = self.schedule_text.get()

        if notification_text and schedule_text:
            try:
                hh, mm = map(int, schedule_text.split(':'))
                current_time = datetime.now().strftime("%H:%M")
                if f"{hh:02}:{mm:02}" >= current_time:
                    schedule.every().day.at(f"{hh:02}:{mm:02}").do(
                        self.show_notification, notification_text, custom_title, custom_message)
                    messagebox.showinfo("Scheduled", f"Notification scheduled for {schedule_text}")
                else:
                    messagebox.showerror("Error", "Invalid time. Please select a future time.")
            except ValueError:
                messagebox.showerror("Error", "Invalid time format. Please use HH:MM format.")
        else:
            messagebox.showerror("Error", "Please enter notification text and schedule time.")

def run_notifier():
    root = tk.Tk()
    app = NotifierGUI(root)
    root.mainloop()

if __name__ == "__main__":
    threading.Thread(target=run_notifier).start()
    while True:
        schedule.run_pending()
