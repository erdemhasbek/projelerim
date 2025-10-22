# Employee Attendance Tracking Application with Punctual Employee System

## Project Description
This is a console-based Python application that allows users to manage employee attendance by recording entry and exit times, setting official work hours, and identifying the most punctual employee based on arrival times. The application uses object-oriented programming and stores data in CSV format.

## Project Structure

<pre>
EmployeeAttendanceSystem/
├── main.py
├── attendance_system.py
├── employee.py
├── attendance_utils.py
├── report_utils.py
│
├── data/
│ ├── employees.csv
│ └── attendance_records.csv
│
├── test_attendance_system.py
├── requirements.txt
└── README.md
 </pre>











## How to Run

1. Make sure you have Python 3.10 or higher installed.
2. Open terminal in the project folder.
3. Run the application:


## To run the automated tests:

python test_attendance_system.py



## Features

- Add new employees
- Record daily attendance (entry and exit)
- Set official work start time
- Automatically calculate delays
- Calculate monthly working hours
- Identify the most punctual employee
- Overtime alert


## Technologies Used

- Python Standard Library:
- datetime
- csv
- os
- collections

## Notes

- All data is stored in the `data/` folder.
- The project is modular, clean, and easy to maintain or extend.
- Attendance and employee information is stored in `.csv` files.
- You can validate all edge cases (invalid dates/times, duplicate IDs, etc.) via test_attendance_system.py.

