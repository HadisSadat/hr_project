import os
import pickle


class SalaryDa:
    def __init__(self):
        self.filename = "data_access/data/salary.dat"
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        self.salary_list = self.find_all()

    def save(self, salary):
        self.salary_list.append(salary)
        file = open(self.filename, "wb")
        pickle.dump(self.salary_list, file)
        file.close()

    def find_all(self):
         if not os.path.exists(self.filename):
            return []
         else:
            file = open(self.filename, "rb")
            salary_list = pickle.load(file)
            file.close()
            return salary_list