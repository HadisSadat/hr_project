from business_logic.attendance_bl import AttendanceBL
from model.attendance import Attendance


class AttendanceController:
    def __init__(self):
        self.attendance_bl = AttendanceBL()



    def save(self, att_id, emp_id, date, check_in, check_out):
        try:
            attendance = Attendance(att_id, emp_id, date, check_in, check_out)
            self.attendance_bl.save(attendance)

            return True, "Attendance Saved Successfully"

        except Exception as e:
            return False, f"Save Failed : {e}"



    def find_all(self):
        try:
            attendance_list = self.attendance_bl.find_all()
            return True, attendance_list
        except Exception as e:
            return False, f"Load Failed : {e}"