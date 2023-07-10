
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
 
 
class AttendanceTracker(QMainWindow):
     def __init__(self):
        super().__init__()

        self.total_classes = 0
        self.attended_classes = 0

        self.setWindowTitle("Attendance Tracker")
        self.setGeometry(300, 300, 300, 200)

        self.label_total_classes = QLabel("Total Classes:", self)
        self.label_total_classes.move(50, 30)
        self.line_total_classes = QLineEdit(self)
        self.line_total_classes.move(150, 30)

        self.label_attended_classes = QLabel("Attended Classes:", self)
        self.label_attended_classes.move(50, 70)
        self.line_attended_classes = QLineEdit(self)
        self.line_attended_classes.move(150, 70)

        self.btn_calculate = QPushButton("Calculate", self)
        self.btn_calculate.move(100, 120)
        self.btn_calculate.clicked.connect(self.calculate_attendance)
 
        self.label_warning = QLabel("", self)
        self.label_warning.move(50, 160)

     def calculate_attendance(self):
        total_classes = int(self.line_total_classes.text())
        attended_classes = int(self.line_attended_classes.text()) 
        if total_classes > 0 and attended_classes >= 0 and attended_classes <= total_classes:
            self.total_classes = total_classes
            self.attended_classes = attended_classes

            attendance_percentage = (attended_classes / total_classes) * 100
            classes_required = 0

            if attendance_percentage < 75:
                classes_required = int((0.75 * total_classes - attended_classes) / 0.25)

                self.label_warning.setText("Warning: Attendance below 75%!")
                self.label_warning.setStyleSheet("color: red")
                self.label_warning.adjustsize()
            else:
                self.label_warning.setText("")

            self.statusBar().showMessage(
                f"Attendance: {attendance_percentage:.2f}%, Classes Required: {classes_required}"
            )
        else:
            self.statusBar().showMessage("Invalid input.")

        self.line_total_classes.clear()
        self.line_attended_classes.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AttendanceTracker()
    window.show()
    sys.exit(app.exec_())
