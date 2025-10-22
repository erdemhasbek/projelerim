from attendance_system import AttendanceSystem
from report_utils import get_most_punctual_employee
from attendance_utils import calculate_monthly_hours

def main():
    system = AttendanceSystem()
    while True:
        print("\n=== Employee Attendance Tracking System ===")
        print("1. Add Employee")
        print("2. Record Attendance")
        print("3. Set Official Work Start Time")
        print("4. Show Punctual Employee of the Month")
        print("5. Calculate Monthly Working Hours")
        print("6. Exit")
        choice = input("Select an option (1-6): ")
        if choice == '1':
            eid = input("Enter Employee ID: ")
            nm = input("Enter Name: ")
            system.add_employee(eid, nm)
        elif choice == '2':
            eid = input("Enter Employee ID: ")
            dt = input("Enter Date (YYYY-MM-DD): ")
            ent = input("Enter Entry Time (HH:MM): ")
            ext = input("Enter Exit Time (HH:MM): ")
            system.record_attendance(eid, dt, ent, ext)
        elif choice == '3':
            ts = input("Enter official work start time (HH:MM): ")
            system.set_work_start_time(ts)
        elif choice == '4':
            if not system.start_time:
                print("❌ Please set official start time first.")
            else:
                month = input("Enter month to evaluate (YYYY-MM): ")
                names, cnt = get_most_punctual_employee(
                    system.record_file,
                    system.start_time,
                    system.emp_file,
                    month
                )
                if names:
                    print(f"🏆 Best Employee(s) in {month} (Late {cnt} time(s)):")
                    for n in names:
                        print(f" - {n}")
                else:
                    print(f"⚠️ No attendance records found for {month}.")
        elif choice == '5':
            eid = input("Enter Employee ID: ")
            month = input("Enter month to evaluate (YYYY-MM): ")
            hours = calculate_monthly_hours(system.record_file, eid, month)
            print(f"🕒 {eid} worked {hours:.1f} hours in {month}.")
            if hours > 160:
                overtime = hours - 160
                print(f"⚠️ This employee worked {overtime:.1f} hours overtime in {month}.")
        elif choice == '6':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number 1-6.")

if __name__ == "__main__":
    main()