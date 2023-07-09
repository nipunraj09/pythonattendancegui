import tkinter as tk
from tkinter import messagebox

class AttendanceTrackerGUI:
    def __init__(self, total_classes):
        self.total_classes = total_classes
        self.attended_classes = 0
        self.attendance_percentage = 0

        self.window = tk.Tk()
        self.window.title("Attendance Tracker")

        self.attended_label = tk.Label(self.window, text="Attended Classes:")
        self.attended_label.pack()

        self.attended_entry = tk.Entry(self.window)
        self.attended_entry.pack()

        self.calculate_button = tk.Button(self.window, text="Calculate", command=self.calculate_attendance)
        self.calculate_button.pack()

    def calculate_attendance(self):
        try:
            self.attended_classes = int(self.attended_entry.get())
            self.attendance_percentage = (self.attended_classes / self.total_classes) * 100
            messagebox.showinfo("Attendance", f"Your attendance: {self.attendance_percentage:.2f}%")

            if self.attendance_percentage < 75:
                classes_needed = int((0.75 * self.total_classes - self.attended_classes) / 0.25)
                messagebox.showwarning("Attendance Warning", f"Your attendance is below 75%.\n"
                                                              f"You need to attend {classes_needed} more classes "
                                                              f"to reach 75% attendance.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of attended classes.")

if __name__ == "__main__":
    total_classes = 40  # Change this value to match the total number of classes in your case
    gui = AttendanceTrackerGUI(total_classes)
    gui.window.mainloop()
