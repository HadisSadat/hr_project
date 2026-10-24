from tkinter import *
from tkinter import ttk, messagebox
from controller.salary_controller import SalaryController

class SalaryView:
    def __init__(self):
        self.controller = SalaryController()

        self.win = Toplevel()
        self.win.geometry("750x350")
        self.win.title("Salaries")

        # Salary ID
        Label(self.win, text="Salary ID").place(x=20, y=20)
        self.salary_id = IntVar()
        Entry(self.win, textvariable=self.salary_id).place(x=120, y=20)

        # Employee ID
        Label(self.win, text="Emp ID").place(x=20, y=60)
        self.emp_id = IntVar()
        Entry(self.win, textvariable=self.emp_id).place(x=120, y=60)

        # Base Salary
        Label(self.win, text="Base Salary").place(x=20, y=100)
        self.base_salary = IntVar()
        Entry(self.win, textvariable=self.base_salary).place(x=120, y=100)

        # Overtime (Hours or Amount)
        Label(self.win, text="Overtime").place(x=20, y=140)
        self.overtime = IntVar()
        Entry(self.win, textvariable=self.overtime).place(x=120, y=140)

        # Bonus
        Label(self.win, text="Bonus").place(x=20, y=180)
        self.bonus = IntVar()
        Entry(self.win, textvariable=self.bonus).place(x=120, y=180)

        # Table
        self.table = ttk.Treeview(self.win, show="headings", columns=[1, 2, 3, 4, 5, 6])
        self.table.place(x=260, y=20, width=470, height=300)

        self.table.column(1, width=60)
        self.table.column(2, width=60)
        self.table.column(3, width=80)
        self.table.column(4, width=70)
        self.table.column(5, width=70)
        self.table.column(6, width=100)

        self.table.heading(1, text="Salary ID")
        self.table.heading(2, text="Emp ID")
        self.table.heading(3, text="Base Salary")
        self.table.heading(4, text="Overtime")
        self.table.heading(5, text="Bonus")
        self.table.heading(6, text="Total")

        self.table.bind("<ButtonRelease>", self.table_click)

        Button(self.win, text="Save", command=self.save_click, width=15).place(x=30, y=300)
        self.reset_from()
        
    def reset_from(self):
        self.salary_id.set(0)
        self.emp_id.set(0)
        self.base_salary.set(0)
        self.overtime.set(0)
        self.bonus.set(0)

        for item in self.table.get_children():
            self.table.delete(item)

        success, data = self.controller.find_all()
        if success:
            for sal in data:
                self.table.insert("", END, values=sal.to_tuple())

        else:
            messagebox.showerror("Load Error", str(data))

    def save_click(self):
        success, message = self.controller.save(
            self.salary_id.get(),
            self.emp_id.get(),
            self.base_salary.get(),
            self.overtime.get(),
            self.bonus.get()
        )

        if success:
            messagebox.showinfo("Success", message)
            self.reset_from()
        else:
            messagebox.showerror("Error", message)

    def table_click(self, event):
        selected = self.table.focus()
        values = self.table.item(selected)["values"]
        if values:
            self.salary_id.set(int(values[0]))
            self.emp_id.set(int(values[1]))
            self.base_salary.set(int(values[2]))
            self.overtime.set(int(values[3]))
            self.bonus.set(int(values[4]))
