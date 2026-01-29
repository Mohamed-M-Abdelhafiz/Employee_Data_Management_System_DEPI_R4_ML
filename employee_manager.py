import csv
import os


class EmployeeManager:
    def __init__(self, filename="employees.csv"):
        self.filename = filename
        self.employees = {}
        self.load_from_csv()

    # -------- Load Data from CSV --------
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

    # -------- Save Data to CSV --------
    def save_to_csv(self):
        with open(self.filename, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["ID", "Name", "Position", "Salary", "Email"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for emp_id in self.employees:
                data = self.employees[emp_id]
                writer.writerow({
                    "ID": emp_id,
                    "Name": data["Name"],
                    "Position": data["Position"],
                    "Salary": data["Salary"],
                    "Email": data["Email"]
                })

    # -------- Add Employee --------
    def add_employee(self):
        emp_id = input("Enter Employee ID: ")

        if emp_id in self.employees:
            print("Employee already exists.")
            return

        name = input("Enter Name: ")
        position = input("Enter Position: ")

        try:
            salary = float(input("Enter Salary: "))
        except ValueError:
            print("Salary must be a number.")
            return

        email = input("Enter Email: ")

        self.employees[emp_id] = {
            "Name": name,
            "Position": position,
            "Salary": salary,
            "Email": email
        }

        self.save_to_csv()
        print("Employee added.")

    # -------- View Employees --------
    def view_employees(self):
        if not self.employees:
            print("No employees found.")
            return

        for emp_id in self.employees:
            data = self.employees[emp_id]
            print("----------------------------")
            print("ID:", emp_id)
            print("Name:", data["Name"])
            print("Position:", data["Position"])
            print("Salary:", data["Salary"])
            print("Email:", data["Email"])

    # -------- Update Employee --------
    def update_employee(self):
        emp_id = input("Enter Employee ID to update: ")

        if emp_id not in self.employees:
            print("Employee not found.")
            return

        print("Press Enter to keep old value.")

        name = input("New Name: ")
        position = input("New Position: ")
        salary = input("New Salary: ")
        email = input("New Email: ")

        if name != "":
            self.employees[emp_id]["Name"] = name
        if position != "":
            self.employees[emp_id]["Position"] = position
        if salary != "":
            try:
                self.employees[emp_id]["Salary"] = float(salary)
            except ValueError:
                print("Invalid salary. Skipped.")
        if email != "":
            self.employees[emp_id]["Email"] = email

        self.save_to_csv()
        print("Employee updated.")

    # -------- Delete Employee --------
    def delete_employee(self):
        emp_id = input("Enter Employee ID to delete: ")

        if emp_id in self.employees:
            del self.employees[emp_id]
            self.save_to_csv()
            print("Employee deleted.")
        else:
            print("Employee not found.")

    # -------- Search Employee --------
    def search_employee(self):
        emp_id = input("Enter Employee ID to search: ")

        if emp_id in self.employees:
            data = self.employees[emp_id]
            print("----------------------------")
            print("ID:", emp_id)
            print("Name:", data["Name"])
            print("Position:", data["Position"])
            print("Salary:", data["Salary"])
            print("Email:", data["Email"])
        else:
            print("Employee not found.")

    # -------- Menu --------
    def menu(self):
        while True:
            print("\nEmployee Management System")
            print("1. Add Employee")
            print("2. View Employees")
            print("3. Update Employee")
            print("4. Delete Employee")
            print("5. Search Employee")
            print("6. Exit")

            choice = input("Choose option (1-6): ")

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
                print("Program ended.")
                break
            else:
                print("Invalid choice.")


# -------- Run Program --------
if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()
