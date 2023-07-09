# pythonattendancegui
Determines attendance
In this code, we create a class called AttendanceTrackerGUI that represents the GUI. The __init__ method sets up the window and widgets. The calculate_attendance method is triggered when the "Calculate" button is pressed. It retrieves the value entered in the text entry field, calculates the attendance percentage, and displays it in a message box.

If the attendance percentage is below 75%, a warning message box is displayed, indicating the number of additional classes required to reach a 75% attendance level. The try-except block handles potential errors if the input is not a valid number.

You can modify the total_classes variable in the if __name__ == "__main__": block to match the total number of classes in your case.
