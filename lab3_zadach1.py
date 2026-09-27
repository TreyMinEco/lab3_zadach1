employees = {
    "Руденко": [12500, "чоловік"],
    "Павленко": [25000, "жінка"],
    "Шевченко": [15550, "чоловік"],
    "Сагайдачний": [17900, "чоловік"],
    "Біла": [23000, "жінка"],
    "Романенко": [16750, "жінка"],
    "Лисенко": [25500, "чоловік"],
    "Слуга": [30000, "чоловік"],
    "Марченко": [22000, "чоловік"],
    "Бондаренко": [28000, "жінка"]
}

def vivid_all(employees):
    print("\nСписок всих співробітників та їх зарплат:")
    for employee in employees:
        print("Прізвіще:", employee, "-", "Зарплата:", employees[employee][0], "грн.,", "Стать:", employees[employee][1])

def add_employee(employees):
    print("\nДодавання нового співробітника:")
    surname = input("Введіть прізвіще нового співробітника: ")
    if surname in employees:
        print(f"Помилка, співробітник із прізвіщем {surname} вже існує! ")
        return
    try:
        salary = float(input(f"Введіть зарплату яка призначена для співробітника {surname}: "))
        if salary <= 0:
            print("Помилка, зарплата не може бути меншою або рівною 0!")
            return
        gender = input(f"Введіть стать співробітнику {surname} (чоловфк/жінка): ")
        if gender != "чоловік" and gender != "жінка":
            print("Помилка, ви увели невірне значення, має бути чоловік/жінка!")
            return

        employees[surname] = [salary, gender]
        print(f"Співробітника {surname}, із зарплатою {salary}, успішно додано до списку!")
    except ValueError:
        print("Помилка, зарплата має бути числом!")

def del_employees(employees):
    print("\nВидалення співробітника")
    surname = input("Введіть прізвіще співробітника: ")
    try:
        del employees[surname]
        print(f"Співробітника {surname} видалено!")
    except KeyError:
        print(f"Помилка, співробітника із прізвіщем {surname} не знайдено!")

def slov_sort(employees):
    print("\nСпівробітники за відсортованими прізвіщами:")
    for employee in sorted(employees):
        print("Прізвіще:", employee, "-", "Зарплата:", employees[employee][0], "грн.,", "Стать:", employees[employee][1])

def max_salary_(employees):
    max_salary = 0
    max_employee = ""
    for employee in employees:
        if employees[employee][0] > max_salary:
            max_salary = employees[employee][0]
            max_employee = employee
    print(f"Максимальну зарплату має співробітик із прізвіщем {max_employee} і розмір зарплати сягає {max_salary} грн")

def min_salary(employees):
    min_man_salary = 0
    min_man = ""
    min_woman_salary = 0
    min_woman = ""

    for employee in employees:
        if employees[employee][1] == "чоловік":
            if min_man_salary == 0 or employees[employee][0] < min_man_salary:
                min_man_salary = employees[employee][0]
                min_man = employee

        if employees[employee][1] == "жінка":
            if min_woman_salary == 0 or employees[employee][0] < min_woman_salary:
                min_woman_salary = employees[employee][0]
                min_woman = employee

    print(f"Чоловік із мінімальною зарплатою {min_man} - {min_man_salary} грн")
    print(f"Жінка із мінімальною зарплатою {min_woman} - {min_woman_salary} грн")

while True:
    print("\nГОЛОВНЕ МЕНЮ:")
    print("1 - Вивести весь список співробітників")
    print("2 - Додати нового співробітника")
    print("3 - Видалити співробітника")
    print("4 - Вивести за відсортованими прізвіщами")
    print("5 - Вивести максимальну зарплату співробітника")
    print("6 - Вивести мінімальну зарплату чоловіка та жінки")
    print("7 - Завершити роботу програми")

    variants = input("Ведіть ваш вибір: ")

    if variants == "1":
        vivid_all(employees)
    elif variants == "2":
        add_employee(employees)
    elif variants == "3":
        del_employees(employees)
    elif variants == "4":
        slov_sort(employees)
    elif variants == "5":
        max_salary_(employees)
    elif variants == "6":
        min_salary(employees)
    elif variants == "7":
        print("Програма завершує роботу!")
        break
    else:
        print("Помилка ви ввели неправильне значення! Спробуйте ще раз")
    