import datetime

# Sample data

students = [
    "Umair Tahir Shareef",
    "Mahati Shri Varenya",
    "Manyatha Deepala",
    "Jaideep Sushanth",
    "Pravallika"
]

attendance = {
    "2024-11-28": {
        "Umair Tahir Shareef": "P",
        "Mahati Shri Varenya": "P",
        "Manyatha Deepala": "A",
        "Jaideep Sushanth": "P",
        "Pravallika": "P"
    },
    "2024-11-29": {
        "Umair Tahir Shareef": "P",
        "Mahati Shri Varenya": "A",
        "Manyatha Deepala": "P",
        "Jaideep Sushanth": "P",
        "Pravallika": "A"
    },
    "2024-11-30": {
        "Umair Tahir Shareef": "A",
        "Mahati Shri Varenya": "P",
        "Manyatha Deepala": "P",
        "Jaideep Sushanth": "P",
        "Pravallika": "P"
    },
    str(datetime.date.today()): {
        "Umair Tahir Shareef": "P",
        "Mahati Shri Varenya": "P",
        "Manyatha Deepala": "P",
        "Jaideep Sushanth": "A",
        "Pravallika": "P"
    }
}


def add_student():
    name = input("Student name: ").strip()

    if name and name not in students:
        students.append(name)
        print(f"Added {name}")
    else:
        print("Invalid or duplicate name")


def delete_student():
    if not students:
        return print("No students")

    print("Students:", ", ".join(students))
    name = input("Delete: ").strip()

    if name in students:
        students.remove(name)
        for date in attendance:
            attendance[date].pop(name, None)
        print(f"Deleted {name}")
    else:
        print("Not found")


def view_students():
    for i, s in enumerate(students, 1):
        print(f"{i}. {s}")


def mark_attendance():
    if not students:
        return print("Add students first")

    date = input("Date (YYYY-MM-DD) or press Enter for today: ").strip() or str(datetime.date.today())

    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except:
        return print("Invalid date format")

    if date not in attendance:
        attendance[date] = {}

    print(f"Marking attendance for {date}")

    for i, student in enumerate(students, 1):
        current = attendance[date].get(student, "")
        status_info = f" [Current: {current}]" if current else ""

        print(f"\n{i}. {student}{status_info}")

        while True:
            status = input("P or A: ").upper().strip()

            if status in ["P", "A"]:
                attendance[date][student] = status
                break

            print("Enter P or A")

    print("Done")


def view_attendance():
    if not attendance:
        return print("No records")

    for date in sorted(attendance.keys(), reverse=True):
        print(f"\n{date}")

        for s, st in attendance[date].items():
            print(f"{s}: {st}")


def daily_summary():
    if not attendance:
        return print("No records")

    date = input("Date (YYYY-MM-DD) or press Enter for today: ").strip() or str(datetime.date.today())

    if date not in attendance:
        return print(f"No record for {date}")

    record = attendance[date]
    p = list(record.values()).count("P")
    a = list(record.values()).count("A")

    print(f"{date}: Total={len(students)}, Present={p} ({p / len(students) * 100:.0f}%), Absent={a}")

    if a:
        print("Absent:", ", ".join([s for s, st in record.items() if st == "A"]))


def student_report():
    if not students:
        return print("No students")

    name = input("Student name: ").strip()

    if name not in students:
        return print("Not found")

    print(f"\n{name}'s Report")

    total = 0
    present = 0

    for date in sorted(attendance.keys()):
        if name in attendance[date]:
            total += 1
            st = attendance[date][name]
            present += (st == "P")
            print(f"{date}: {st}")

    if total:
        print(
            f"\nTotal days: {total}, Present: {present}, "
            f"Absent: {total - present}, Rate: {present / total * 100:.0f}%"
        )


def edit_attendance():
    if not attendance:
        return print("No records")

    date = input("Date (YYYY-MM-DD): ").strip()

    if date not in attendance:
        return print("Date not found")

    print(f"\nAttendance for {date}:")
    for s, st in attendance[date].items():
        print(f"{s}: {st}")

    student = input("\nStudent to edit: ").strip()

    if student not in attendance[date]:
        return print("Not found")

    while True:
        new = input("New status (P/A): ").upper().strip()

        if new in ["P", "A"]:
            attendance[date][student] = new
            print(f"Updated to {new}")
            break


def delete_date():
    if not attendance:
        return print("No records")

    for date in sorted(attendance.keys(), reverse=True):
        print(date)

    date = input("\nDelete date: ").strip()

    if date not in attendance:
        return print("Not found")

    if input(f"Delete {date}? (yes/no): ").lower() == "yes":
        del attendance[date]
        print("Deleted")


def view_range():
    if not attendance:
        return print("No records")

    start = input("Start (YYYY-MM-DD): ").strip()
    end = input("End (YYYY-MM-DD): ").strip()

    try:
        s_date = datetime.datetime.strptime(start, "%Y-%m-%d").date()
        e_date = datetime.datetime.strptime(end, "%Y-%m-%d").date()
    except:
        return print("Invalid dates")

    print(f"\n{start} to {end}")

    for date in sorted(attendance.keys()):
        d = datetime.datetime.strptime(date, "%Y-%m-%d").date()

        if s_date <= d <= e_date:
            record = attendance[date]
            p = list(record.values()).count("P")
            a = list(record.values()).count("A")

            print(f"\n{date} (P:{p} A:{a})")

            for s, st in record.items():
                print(f"{s}: {st}")


def copy_date():
    if not attendance:
        return print("No records")

    source = input("Copy from (YYYY-MM-DD): ").strip()

    if source not in attendance:
        return print("Not found")

    target = input("Copy to (YYYY-MM-DD): ").strip()

    try:
        datetime.datetime.strptime(target, "%Y-%m-%d")
    except:
        return print("Invalid date")

    if target in attendance and input(f"{target} exists. Overwrite? (yes/no): ").lower() != "yes":
        return print("Cancelled")

    attendance[target] = attendance[source].copy()
    print(f"Copied {source} to {target}")


def save():
    with open("attendance_data.txt", "w") as f:
        f.write("STUDENTS:\n")

        for i, s in enumerate(students, 1):
            f.write(f"{i}. {s}\n")

        f.write("\nATTENDANCE:\n")

        for date in sorted(attendance.keys(), reverse=True):
            p = list(attendance[date].values()).count("P")
            a = list(attendance[date].values()).count("A")

            f.write(f"\n{date} (P:{p} A:{a}):\n")

            for s, st in attendance[date].items():
                f.write(f"{s}: {st}\n")

    print("Saved to attendance_data.txt")


def reset():
    global students, attendance

    if input("Reset to sample data? (yes/no): ").lower() == "yes":
        students.clear()
        students.extend([
            "Umair Tahir Shareef",
            "Mahati Shri Varenya",
            "Manyatha Deepala",
            "Jaideep Sushanth",
            "Pravallika"
        ])

        attendance.clear()
        attendance.update({
            "2024-11-28": {
                "Umair Tahir Shareef": "P",
                "Mahati Shri Varenya": "P",
                "Manyatha Deepala": "A",
                "Jaideep Sushanth": "P",
                "Pravallika": "P"
            },
            "2024-11-29": {
                "Umair Tahir Shareef": "P",
                "Mahati Shri Varenya": "A",
                "Manyatha Deepala": "P",
                "Jaideep Sushanth": "P",
                "Pravallika": "A"
            },
            "2024-11-30": {
                "Umair Tahir Shareef": "A",
                "Mahati Shri Varenya": "P",
                "Manyatha Deepala": "P",
                "Jaideep Sushanth": "P",
                "Pravallika": "P"
            },
            str(datetime.date.today()): {
                "Umair Tahir Shareef": "P",
                "Mahati Shri Varenya": "P",
                "Manyatha Deepala": "P",
                "Jaideep Sushanth": "A",
                "Pravallika": "P"
            }
        })

        print("Reset done")


menu = {
    "1": ("Add Student", add_student),
    "2": ("Delete Student", delete_student),
    "3": ("View Students", view_students),
    "4": ("Mark Attendance", mark_attendance),
    "5": ("View Attendance", view_attendance),
    "6": ("Daily Summary", daily_summary),
    "7": ("Student Report", student_report),
    "8": ("Edit Attendance", edit_attendance),
    "9": ("Delete Date", delete_date),
    "10": ("View Date Range", view_range),
    "11": ("Copy Date", copy_date),
    "12": ("Save to File", save),
    "13": ("Reset Data", reset),
    "14": ("Exit", None)
}

print("ATTENDANCE MANAGEMENT SYSTEM")
print("Loaded with 5 sample students")

while True:
    for k, (name, _) in menu.items():
        print(f"{k}. {name}")

    choice = input("Choose (1-14): ").strip()

    if choice == "14":
        print("Thank you!")
        break

    elif choice in menu:
        menu[choice][1]()

    else:
        print("Invalid choice")