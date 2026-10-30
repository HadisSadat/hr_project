from business_logic.department_bl import DepartmentBL
from model.department import Department


class DepartmentController:
    def __init__(self):
        self.department_bl = DepartmentBL()



    def save(self, dep_id, department_name):
        try:
            department = Department(dep_id, department_name)
            self.department_bl.save(department)

            return True, "Department Saved"

        except Exception as e:
            return False, f"Save Failed : {e}"



    def find_all(self):
        try:
            department_list = self.department_bl.find_all()
            return True, department_list
        except Exception as e:
            return False, f"Load Failed : {e}"