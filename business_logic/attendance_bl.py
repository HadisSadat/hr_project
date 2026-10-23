from data_access.attendance_da import AttendanceDa
from data_access.employee_da import EmployeeDa

class AttendanceBL:
    def __init__(self):
        self.attendance_da = AttendanceDa()
        self.employee_da = EmployeeDa()

    def save(self, attendance):
        employees = [emp.emp_id for emp in self.employee_da.find_all()]
        if attendance.emp_id not in employees:
            raise ValueError("Employee ID does not exist.")

        if attendance.check_in >= attendance.check_out:
            raise ValueError("Check-out time must be after check-in time.")
        try:
            attendance.calculate_hour()
        except Exception as e:
            raise ValueError(f"Time format error: {e}")


        self.attendance_da.save(attendance)

    def find_all(self):
        return self.attendance_da.find_all()