import os
import pickle


class DepartmentDa:
    def __init__(self):
        self.filename = "data_access/data/departments.dat"
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        self.department_list = self.find_all()

    def save(self, department):
        self.department_list.append(department)
        file = open(self.filename, "wb")
        pickle.dump(self.department_list, file)
        file.close()

    def find_all(self):
         if not os.path.exists(self.filename):
            return []
         else:
            file = open(self.filename, "rb")
            department_list = pickle.load(file)
            file.close()
            return department_list