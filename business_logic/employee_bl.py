from data_access.employee_da import EmployeeDa
from data_access.department_da import DepartmentDa


class EmployeeBL:
    def __init__(self):
        self.employee_da = EmployeeDa()
        self.department_da = DepartmentDa()

    def save(self, employee):
        employees = self.employee_da.find_all()
        for emp in employees:
            if emp.emp_id == employee.emp_id:
                raise ValueError("Employee ID already exists!")
            if emp.national_id == employee.national_id:
                raise ValueError("National ID already exists!")
        deps = [d.dep_id for d in self.department_da.find_all()]
        if employee.dep_id not in deps and employee.dep_id != 0:
            raise ValueError("Department ID does not exist")

        self.employee_da.save(employee)

    def find_all(self):
        return self.employee_da.find_all()