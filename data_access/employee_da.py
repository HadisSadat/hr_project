import os
import pickle


class EmployeeDa:
    def __init__(self):
        self.filename = "data_access/data/employees.dat"
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        self.employee_list = self.find_all()

    def save(self, employee):
        self.employee_list.append(employee)
        file = open(self.filename, "wb")
        pickle.dump(self.employee_list, file)
        file.close()

    def find_all(self):
         if not os.path.exists(self.filename):
            return []
         else:
            file = open(self.filename, "rb")
            employee_list = pickle.load(file)
            file.close()
            return employee_list