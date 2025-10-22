import csv
from collections import defaultdict
from datetime import datetime

def calculate_lateness_count(record_file, start_time, month=None):
    lateness_count = defaultdict(int)
    try:
        with open(record_file, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                date = row.get("Date")
                emp_id = row.get("Employee ID")
                entry = row.get("Entry Time")
                if not date or not emp_id or not entry:
                    continue
                if month and not date.startswith(month + "-"):
                    continue
                _ = lateness_count[emp_id]
                try:
                    entry_time = datetime.strptime(entry, "%H:%M")
                    official = datetime.strptime(start_time, "%H:%M")
                except ValueError:
                    print(f"⚠️ Invalid time format in record: {entry}")
                    continue
                if entry_time > official:
                    lateness_count[emp_id] += 1
    except FileNotFoundError:
        print(f"❌ Attendance records file not found: {record_file}")
    except Exception as e:
        print(f"❌ Error reading attendance records: {e}")
    return lateness_count


def calculate_monthly_hours(record_file, emp_id, month):
    total_hours = 0.0
    try:
        with open(record_file, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get('Employee ID') != emp_id:
                    continue
                date = row.get('Date')
                if not date or not date.startswith(month + "-"):
                    continue
                entry = row.get('Entry Time')
                exit_ = row.get('Exit Time')
                try:
                    t1 = datetime.strptime(entry, "%H:%M")
                    t2 = datetime.strptime(exit_, "%H:%M")
                except ValueError:
                    print(f"⚠️ Invalid time format for entry/exit: {entry}/{exit_}")
                    continue
                total_hours += (t2 - t1).total_seconds() / 3600
    except FileNotFoundError:
        print(f"❌ Attendance records file not found: {record_file}")
    except Exception as e:
        print(f"❌ Error reading attendance records: {e}")
    return total_hours