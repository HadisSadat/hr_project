from business_logic.salary_bl import SalaryBL
from model.salary import Salary


class SalaryController:
    def __init__(self):
        self.salary_bl = SalaryBL()

    def save(self, salary_id, emp_id, base_salary, overtime, bonus):
        try:
            salary = Salary(salary_id, emp_id, base_salary, overtime, bonus)

            self.salary_bl.save(salary)

            return True, "Salary Saved Successfully"

        except Exception as e:
            return False, f"Save Failed : {e}"

    def find_all(self):
        try:
            salary_list = self.salary_bl.find_all()
            return True, salary_list
        except Exception as e:
            return False, f"Load Failed : {e}"