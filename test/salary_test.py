from model.salary import Salary
from model.employee import Employee

from data_access.salary_da import SalaryDa
from data_access.employee_da import EmployeeDa
from business_logic.salary_bl import SalaryBL
from controller.salary_controller import SalaryController



employee_da = EmployeeDa()
employee_1 = Employee(emp_id=1, name="Reza", family="Bayat", national_id="0015225141", phone_number="09123880399", position="manager", salary=10000, dep_id=10)
employee_da.save(employee_1)
print("Employee 1 Saved.")



salary_1 = Salary(salary_id=1, emp_id=1, base_salary=10000000, overtime=5, bonus=500000)
print(salary_1)
print(salary_1.to_tuple())



salary_da = SalaryDa()
print(salary_da.find_all())
salary_da.save(salary_1)
print(salary_da.find_all())



bl = SalaryBL()
print(bl.find_all())
print(bl.employee_da.find_all())


controller = SalaryController()
success, message = controller.save(salary_id=2, emp_id=1, base_salary=12000000, overtime=10, bonus=1000000)
print(success, message)
success, data = controller.find_all()
print(success, data)