from model.department import Department
from data_access.department_da import DepartmentDa
from business_logic.department_bl import DepartmentBL
from controller.department_controller import DepartmentController


dep_da = DepartmentDa()
dep_1 = Department(10, "IT")
print(dep_1)
print(dep_1.to_tuple())




department_da = DepartmentDa()
print(department_da.find_all())
department_da.save(dep_1)
print(department_da.find_all())



bl = DepartmentBL()
print(bl.find_all())
bl.save(Department(3, "Sales"))
print(bl.find_all())



controller = DepartmentController()
success, message = controller.save(dep_id=5, department_name="Finance")
print(success, message)
success, data = controller.find_all()
print()
if success:
    for dep in data:
        print(dep)
else:
    print(data)