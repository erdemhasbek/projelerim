import csv

def get_most_punctual_employee(record_file, start_time, emp_file, month=None):
    from attendance_utils import calculate_lateness_count
    lateness = calculate_lateness_count(record_file, start_time, month)
    if not lateness:
        return [], 0
    min_late = min(lateness.values())
    best_ids = [eid for eid, cnt in lateness.items() if cnt == min_late]
    names = []
    try:
        with open(emp_file, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get('Employee ID') in best_ids:
                    names.append(row.get('Name'))
    except FileNotFoundError:
        print(f"❌ Employee file not found: {emp_file}")
    except Exception as e:
        print(f"❌ Error reading employee file: {e}")
        return [], 0
    return names, min_late