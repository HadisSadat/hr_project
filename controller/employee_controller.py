from business_logic.employee_bl import EmployeeBL
from model.employee import Employee

class EmployeeController:
    def __init__(self):
        self.employee_bl = EmployeeBL()

    def save(self, emp_id, name, national_id, phone, position, salary, dep_id):
        try:
            employee = Employee(emp_id, name, national_id, phone, position, salary, dep_id)
            self.employee_bl.save(employee)
            return True, "Employee Saved"
        except Exception as e:
            return False, f"Save Failed : {e}"

    def find_all(self):
        try:
            employee_list = self.employee_bl.find_all()
            return True, employee_list
        except Exception as e:
            return False, f"Load Failed : {e}"