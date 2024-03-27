from app.company import Company
from app.utility_functions import *


def main():
    company = Company()
    company.load_data("company_data.json")

    department_options = {
        '1': add_department,
        '2': remove_department,
        '3': list_departments,
    }

    employee_options = {
        '1': add_employee,
        '2': remove_employee,
        '3': list_employees_by_department,
    }

    main_menu = {
        '1': department_options,
        '2': employee_options,
    }

    while True:
        print("\n ---- MAIN LIST ----\n")
        print("1. Department Data")
        print("2. Employee Data")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == '2':
            list_departments(company)
        if choice == '3':
            print("Exiting program.")
            break

        if choice in main_menu:
            sub_menu = main_menu[choice]

            while True:
                print("\n --- SUB LIST ---\n")
                print("1. Add")
                print("2. Remove")
                print("3. List")
                print("4. Back to Main")

                sub_choice = input("Enter your choice: ")

                if sub_choice == '4':
                    break

                if sub_choice in sub_menu:
                    sub_menu[sub_choice](company)
                    if sub_choice == '1':
                        save_data(company)
                else:
                    print("Invalid choice. Please enter a valid option.")
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
