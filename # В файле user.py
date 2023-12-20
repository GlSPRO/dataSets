from Scripts.main import mains, UserDataProcessor

UserDataProcessor()

mains()

from RodClass import Table
from prettytable import PrettyTable

class AdministratorDataProcessor:
    def __init__(self):
        self.username = input("Введите ваше имя: ")
        self.role = "Администратор"  # Предполагаю, что роль всегда "Администратор"

class EmployeeTable_Administrator(Table):
    def __init__(self):
        headers = ["Роль", "Имя", "Зарплата", "Часы работы"]
        super().__init__(headers)

    def add_employee(self, name, salary, hours_worked):
        # Получаем роль и имя из AdministratorDataProcessor
        role = "Администратор"
        # Создаем данные для строки и добавляем в родительскую таблицу
        employee_data = [role, name, salary, hours_worked]
        super().add_row(employee_data)

# Создание экземпляра AdministratorDataProcessor
employee_data_processor = AdministratorDataProcessor()

# Создание экземпляра EmployeeTable_Administrator
employee_table_Administrator = EmployeeTable_Administrator()

# Добавление данных с новым атрибутом
employee_table_Administrator.add_employee(employee_data_processor.username, 50000, 40)
employee_table_Administrator.add_employee("Мария", 60000, 35)
employee_table_Administrator.add_employee("Петр", 55000, 38)

# Вывод таблицы
employee_table_Administrator.display_table()

class UserDataProcessor:

    def __init__(self):
        self.username = ""
        self.password = ""
        self.role = ""
        self.apdateUsers = ""

    def process_user_input(self):
        self.username = input("Введите ваше имя: ")
        self.role = input("Введите вашу роль: ")
        self.password = input("Введите ваш пароль: ")

        from Master import employee_table_Master, user_data_handlerss
        from Client import employee_table_Client, ClientDataProcessor, EmployeeTable_Client, \
            user_data_handlers
        from p import employee_table_Administrator, AdministratorDataProcessor

    # def display_user_data(self):
        if user_data_handler.role == "Admin":
            employee_table = AdministratorDataProcessor()
            employee_table_Administrator.display_table()

        if user_data_handler.role == "Client":
            user_data_handlers = ClientDataProcessor()
            employee_table_Client.display_table()

        if user_data_handlerss.role == "Master":
            employee_table_Master.display_table_Master()


user_data_handler = UserDataProcessor()

user_data_handler.process_user_input()

user_data_handler.display_user_data()




# class UNIT:
#
#     def user_data_handlersss(self):


class mains:
    user_data_unite = UNIT()

    user_data_unite.user_data_handlersss()



from RodClass import Table
from prettytable import PrettyTable

class AdministratorDataProcessor:
    def __init__(self):
        self.username = input("Введите ваше имя: ")
        self.role = "Мастер"


class EmployeeTable_Master(Table):
    def __init__(self):
        headers = ["Роль", "Имя", "Список клиентов", "Вид услуги", "Цена", "Время (час)"]
        super().__init__(headers)

    def add_employee(self, role, name, list_klient, vid_uslugi, price, time):
        role = "Мастер"
        employee_data = ([role, name, list_klient, vid_uslugi, price, time])


# Создание экземпляра таблицы
user_data_handlerss = MasterDataProcessor()
employee_table_Master = EmployeeTable_Master()

# Добавление данных
employee_table_Master.add_employee("Мастер", user_data_handlerss.username, "Олеся", "Сведение тату", 7000, 2)
employee_table_Master.add_employee("", "", "Сергей", "Сведение тату", 7000, 1)
employee_table_Master.add_employee("", "", "Владимир", "Сведение тату", 7000, 3)

employee_table_Master.display_table()

from prettytable import PrettyTable

class Table:
    def __init__(self, headers):
        self.table_data = []
        self.table = PrettyTable()
        self.table.field_names = headers

    def add_row(self, data):
        self.table_data.append(data)

    def display_table(self):
        print("\t".join(self.table.field_names))
        print("-" * (8 * len(self.table.field_names)))
        for row in self.table_data:
            print("\t".join(map(str, row)))

from prettytable import PrettyTable
from RodClass import Table

class ClientDataProcessor:
    def __init__(self):
        self.username = ("")
        self.role = ("")
class EmployeeTable_Client(Table):
    def __init__(self):
        headers = ["Роль", "Имя", "Список мастеров", "Вид услуги", "Цена"]
        super().__init__(headers)

    def add_employee(self, role, name, list_masters, vid_uslugi, price):
        self.table.add_row([role, name, list_masters, vid_uslugi, price])


# Создание экземпляра таблицы
user_data_handlers = ClientDataProcessor()
employee_table_Client = EmployeeTable_Client()

# Добавление данных
employee_table_Client.add_employee("Клиент", user_data_handlers.username, "Антон", "Сведение тату", 7000)
employee_table_Client.add_employee("", "", "Роберт", "Новое тату", 5550)
employee_table_Client.add_employee("", "", "Олеся", "Пирсинг", 1500)

employee_table_Client.display_table()