from tkinter import *
from view.employee_view import EmployeeView
from view.department_view import DepartmentView
from view.salary_view import SalaryView
from view.attedance_view import AttendanceView

class PanelView:
    def departments_click(self):
        DepartmentView()

    def employees_click(self):
        EmployeeView()

    def attendance_click(self):
        AttendanceView()

    def salaries_click(self):
        SalaryView()

    def __init__(self):
        self.win = Tk()
        self.win.geometry("350x250")
        self.win.title("HR Panel")

        Button(self.win, text="Departments", command=self.departments_click, width=20).place(x=100, y=30)
        Button(self.win, text="Employees", command=self.employees_click, width=20).place(x=100, y=80)
        Button(self.win, text="Attendance", command=self.attendance_click, width=20).place(x=100, y=130)
        Button(self.win, text="Salaries", command=self.salaries_click, width=20).place(x=100, y=180)

        self.win.mainloop()