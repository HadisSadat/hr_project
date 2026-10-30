from data_access.department_da import DepartmentDa


class DepartmentBL:
    def __init__(self):
        self.department_da = DepartmentDa()



    def save(self, department):
        all_deps = self.department_da.find_all()
        for dep in all_deps:
            if dep.dep_id == department.dep_id:
                raise ValueError("Department ID already exists!")
            if dep.department_name.casefold() == department.department_name.casefold():
                raise ValueError("Department name already exists!")

        self.department_da.save(department)



    def find_all(self):
        return self.department_da.find_all()