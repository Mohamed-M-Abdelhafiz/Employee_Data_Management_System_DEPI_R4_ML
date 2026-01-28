import csv
import os
import re


class EmployeeManager:
    def __init__(self, filename="employees.csv"):
        self.filename = filename
        self.employees = {}
        self.load_from_csv()

    # ---------- File Handling ----------
    def load_from_csv(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.employees[row["ID"]] = {
                    "Name": row["Name"],
                    "Position": row["Position"],
                    "Salary": float(row["Salary"]),
                    "Email": row["Email"]
                }

    def save_to_csv(self):
        with open(self.filename, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["ID", "Name", "Position", "Salary", "Email"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for emp_id, data in self.employees.items():
                writer.writerow({
                    "ID": emp_id,
                    "Name": data["Name"],
                    "Position": data["Position"],
                    "Salary": data["Salary"],
                    "Email": data["Email"]
                })

    # ---------- Validation ----------
    def is_valid_email(self, email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

    # ---------- CRUD Operations ----------
    def add_employee(self):
        emp_id = input("Enter Employee ID: ").strip()

        if emp_id in self.employees:
            print("Employee ID already exists.")
            return

        name = input("Enter Name: ").strip()
        position = input("Enter Position: ").strip()

        try:
            salary = float(input("Enter Salary: "))
        except ValueError:
            print("Salary must be a number.")
            return

        email = input("Enter Email: ").strip()
        if not self.is_valid_email(email):
            print("Invalid email format.")
            return

        self.employees[emp_id] = {
            "Name": name,
            "Position": position,
            "Salary": salary,
            "Email": email
        }

        self.save_to_csv()
        print("Employee added successfully.")

    def view_employees(self):
        if not self.employees:
            print("No employees found.")
            return

        for emp_id, data in self.employees.items():
            print("-" * 35)
            print(f"ID       : {emp_id}")
            print(f"Name     : {data['Name']}")
            print(f"Position : {data['Position']}")
            print(f"Salary   : {data['Salary']}")
            print(f"Email    : {data['Email']}")

    def update_employee(self):
        emp_id = input("Enter Employee ID to update: ").strip()

        if emp_id not in self.employees:
            print("Employee not found.")
            return

        print("Leave any field empty to keep current value.")

        name = input("New Name: ").strip()
        position = input("New Position: ").strip()
        salary = input("New Salary: ").strip()
        email = input("New Email: ").strip()

        if name:
            self.employees[emp_id]["Name"] = name
        if position:
            self.employees[emp_id]["Position"] = position
        if salary:
            try:
                self.employees[emp_id]["Salary"] = float(salary)
            except ValueError:
                print("Invalid salary. Update skipped.")
        if email:
            if self.is_valid_email(email):
                self.employees[emp_id]["Email"] = email
            else:
                print("Invalid email. Update skipped.")

        self.save_to_csv()
        print("Employee updated successfully.")

    def delete_employee(self):
        emp_id = input("Enter Employee ID to delete: ").strip()

        if emp_id in self.employees:
            del self.employees[emp_id]
            self.save_to_csv()
            print("Employee deleted successfully.")
        else:
            print("Employee not found.")

    def search_employee(self):
        emp_id = input("Enter Employee ID to search: ").strip()

        if emp_id in self.employees:
            data = self.employees[emp_id]
            print("-" * 35)
            print(f"ID       : {emp_id}")
            print(f"Name     : {data['Name']}")
            print(f"Position : {data['Position']}")
            print(f"Salary   : {data['Salary']}")
            print(f"Email    : {data['Email']}")
        else:
            print("Employee not found.")

    # ---------- Menu ----------
    def menu(self):
        while True:
            print("\nEmployee Management System")
            print("1. Add Employee")
            print("2. View All Employees")
            print("3. Update Employee")
            print("4. Delete Employee")
            print("5. Search Employee")
            print("6. Exit")

            choice = input("Choose an option (1-6): ").strip()

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_employees()
            elif choice == "3":
                self.update_employee()
            elif choice == "4":
                self.delete_employee()
            elif choice == "5":
                self.search_employee()
            elif choice == "6":
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Try again.")


# ---------- Run Program ----------
if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()
