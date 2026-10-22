from model.employee import Employee

from data_access.employee_da import EmployeeDa
from business_logic.employee_bl import EmployeeBL

from controller.employee_controller import EmployeeController


employee_1 = Employee(1, "Reza", "Bayat", "0015225141", "09123880399", "manager", "10000" )
print(employee_1)
print(employee_1.to_tuple())
employee_2 = Employee(2, "ali4", "mohammadi", "1145732151", "09198562433", "sales employee", "5000")
print(employee_2)
employee_3 = Employee(3, "Omid", "Akbari", "67548231", "09378182465", "crow", "1000")
print(employee_3)



employee_da = EmployeeDa()
print(employee_da.find_all())
employee_da.save(employee_1)
print(employee_da.find_all())



bl = EmployeeBL()
print(bl.find_all())
print(bl.department_da.find_all())




controller = EmployeeController()


result, message = controller.save(1, "Reza", "0015225141", "09123880399", "manager", 10000, 1)
print(result, message)


status, data = controller.find_all()
print(status)
print(data)



