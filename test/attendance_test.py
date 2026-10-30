from model.employee import Employee
from data_access.employee_da import EmployeeDa
from controller.attendance_controller import AttendanceController



emp_da = EmployeeDa()
emp_1 = Employee(emp_id=1, name="Reza", family="Bayat", national_id="0015225141", phone_number="09123880399", position="manager", salary=10000, dep_id=10)
emp_da.save(emp_1)
print("Employee 1 Saved.")




controller = AttendanceController()
success, data = controller.find_all()
print(success, data)



success, message = controller.save(
    att_id=1,
    emp_id=1,
    date="2023-10-25",
    check_in="08:30",
    check_out="17:00"
)
print(success, message)