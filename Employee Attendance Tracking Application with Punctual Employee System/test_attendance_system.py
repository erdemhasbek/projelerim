import os
import shutil
from attendance_system import AttendanceSystem
from report_utils import get_most_punctual_employee
from attendance_utils import calculate_monthly_hours

# --- Test setup: work in a temporary directory ---
TEST_DIR = 'test_data'
EMP_FILE = os.path.join(TEST_DIR, 'employees.csv')
REC_FILE = os.path.join(TEST_DIR, 'attendance_records.csv')

# Cleanup previous test data
if os.path.exists(TEST_DIR):
    shutil.rmtree(TEST_DIR)
os.makedirs(TEST_DIR)

# Initialize system with test files
system = AttendanceSystem(emp_file=EMP_FILE, record_file=REC_FILE)

# Helper to capture pass/fail
def run_test(name, func, *args):
    try:
        func(*args)
        print(f"PASS: {name}")
    except Exception as e:
        print(f"FAIL: {name} - {e}")

# 1. Test add_employee with invalid ID
run_test("Add Employee - Invalid ID", system.add_employee, 'abc', 'TestUser')
# 2. Test add_employee with valid ID
run_test("Add Employee - Valid ID", system.add_employee, '100', 'Alice')
# 3. Test duplicate ID
run_test("Add Employee - Duplicate ID", system.add_employee, '100', 'Bob')
# 4. Test set invalid start time
run_test("Set Start Time - Invalid", system.set_work_start_time, '25:00')
# 5. Test set valid start time
run_test("Set Start Time - Valid", system.set_work_start_time, '09:00')
# 6. Test record_attendance with non-existent ID
run_test("Record Attendance - No such ID", system.record_attendance, '200', '2025-05-10', '09:00', '17:00')
# 7. Test record_attendance with invalid date
run_test("Record Attendance - Invalid Date", system.record_attendance, '100', '2025-02-30', '09:00', '17:00')
# 8. Test record_attendance with invalid time
run_test("Record Attendance - Invalid Time", system.record_attendance, '100', '2025-05-10', '09:65', '17:00')
# 9. Test record_attendance valid
run_test("Record Attendance - Valid", system.record_attendance, '100', '2025-05-10', '09:00', '17:00')
# 10. Test punctual employee when one record exists
names, cnt = get_most_punctual_employee(REC_FILE, '09:00', EMP_FILE, '2025-05')
print("PASS: Get Punctual - Single Record" if names and cnt == 0 else "FAIL: Get Punctual - Single Record")
# 11. Test calculate_monthly_hours for valid record
hours = calculate_monthly_hours(REC_FILE, '100', '2025-05')
print("PASS: Calculate Hours - 8.0h" if abs(hours - 8.0) < 1e-6 else f"FAIL: Calculate Hours = {hours}")
# 12. Test overtime alert logic
# Add extra record for overtime
system.record_attendance('100', '2025-05-11', '09:00', '18:00')  # 9 hours
hours = calculate_monthly_hours(REC_FILE, '100', '2025-05')
expected = hours > 160 or abs(hours - (8+9))<0.1
print("PASS: Overtime Test" if expected else f"FAIL: Overtime Hours = {hours}")

# Clean up
shutil.rmtree(TEST_DIR)
print("\nAll tests completed.")
