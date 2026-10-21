from model.employee import Employee

employee_1 = Employee(1, "Reza", "Bayat", "0015225141", "09123880399", "manager", "10000" )
print(employee_1)
print(employee_1.to_tuple())
employee_2 = Employee(2, "ali4", "mohammadi", "1145732151", "09198562433", "sales employee", "5000")
print(employee_2)
employee_3 = Employee(3, "Omid", "Akbari", "67548231", "09378182465", "crow", "1000")
print(employee_3)