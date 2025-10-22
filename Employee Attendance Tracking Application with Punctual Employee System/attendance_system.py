import csv
import os
from datetime import datetime
from employee import Employee

class AttendanceSystem:
    def __init__(self, emp_file='data/employees.csv', record_file='data/attendance_records.csv'):
        self.emp_file = emp_file
        self.record_file = record_file
        self.start_time = None
        os.makedirs(os.path.dirname(self.emp_file), exist_ok=True)
        for path, headers in [
            (self.emp_file, ["Employee ID", "Name"]),
            (self.record_file, ["Employee ID", "Date", "Entry Time", "Exit Time"])
        ]:
            if not os.path.exists(path):
                with open(path, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(headers)

    def add_employee(self, emp_id, name):
        if not emp_id.isdigit():
            print("❌ Invalid Employee ID. Please enter numbers only.")
            return
        try:
            with open(self.emp_file, newline='') as f:
                for row in csv.DictReader(f):
                    if row.get('Employee ID') == emp_id:
                        print("❌ Employee ID already exists.")
                        return
        except Exception:
            pass
        try:
            with open(self.emp_file, 'a', newline='') as f:
                csv.DictWriter(f, fieldnames=["Employee ID", "Name"]).writerow(
                    Employee(emp_id, name).to_dict()
                )
            print("✅ Employee added successfully.")
        except Exception as e:
            print(f"❌ Error adding employee: {e}")

    def set_work_start_time(self, time_str):
        try:
            datetime.strptime(time_str, "%H:%M")
            self.start_time = time_str
            print(f"✅ Work start time set to {time_str}.")
        except ValueError:
            print("❌ Invalid time format. Please use HH:MM.")

    def record_attendance(self, emp_id, date_str, entry_str, exit_str):
        # ID must be numeric and exist
        if not emp_id.isdigit():
            print("❌ Invalid Employee ID. Please enter numbers only.")
            return
        try:
            with open(self.emp_file, newline='') as f:
                if emp_id not in [r.get('Employee ID') for r in csv.DictReader(f)]:
                    print("❌ Employee ID not found. Please add employee first.")
                    return
        except Exception:
            pass
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            datetime.strptime(entry_str, "%H:%M")
            datetime.strptime(exit_str, "%H:%M")
            with open(self.record_file, 'a', newline='') as f:
                csv.DictWriter(
                    f,
                    fieldnames=["Employee ID", "Date", "Entry Time", "Exit Time"]
                ).writerow({
                    "Employee ID": emp_id,
                    "Date": date_str,
                    "Entry Time": entry_str,
                    "Exit Time": exit_str
                })
            print("✅ Attendance recorded.")
        except ValueError:
            print("❌ Invalid date or time format. Use YYYY-MM-DD and HH:MM.")
        except Exception as e:
            print(f"❌ Error recording attendance: {e}")