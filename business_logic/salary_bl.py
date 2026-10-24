from data_access.salary_da import SalaryDa
from data_access.employee_da import EmployeeDa


class SalaryBL:
    def __init__(self):
        self.salary_da = SalaryDa()
        self.employee_da = EmployeeDa()

    def save(self, salary):
        salaries = self.salary_da.find_all()
        if any(item.salary_id == salary.salary_id for item in salaries):
            raise ValueError("Salary ID already exists!")

        employees = [emp.emp_id for emp in self.employee_da.find_all()]
        if salary.emp_id not in employees:
            raise ValueError("Employee ID does not exist. Cannot assign salary.")

        # Validate values before saving, so rendering the table cannot fail later.
        salary.calculate_total()
        self.salary_da.save(salary)

    def find_all(self):
        return self.salary_da.find_all()