from tkinter import *
from tkinter import ttk, messagebox
from controller.employee_controller import EmployeeController


class EmployeeView:
    def __init__(self):
        self.controller = EmployeeController()

        self.win = Toplevel()
        self.win.geometry("880x450")
        self.win.title("Employees")

        # Emp ID
        Label(self.win, text="Emp ID").place(x=20, y=20)
        self.emp_id = IntVar()
        Entry(self.win, textvariable=self.emp_id).place(x=120, y=20)

        # Name
        Label(self.win, text="Name").place(x=20, y=60)
        self.name = StringVar()
        Entry(self.win, textvariable=self.name).place(x=120, y=60)

        # Family
        Label(self.win, text="Family").place(x=20, y=100)
        self.family = StringVar()
        Entry(self.win, textvariable=self.family).place(x=120, y=100)

        # National ID
        Label(self.win, text="National ID").place(x=20, y=140)
        self.national_id = StringVar()
        Entry(self.win, textvariable=self.national_id).place(x=120, y=140)

        # Phone
        Label(self.win, text="Phone").place(x=20, y=180)
        self.phone = StringVar()
        Entry(self.win, textvariable=self.phone).place(x=120, y=180)

        # Position
        Label(self.win, text="Position").place(x=20, y=220)
        self.position = StringVar()
        Entry(self.win, textvariable=self.position).place(x=120, y=220)

        # Salary
        Label(self.win, text="Base Salary").place(x=20, y=260)
        self.salary = IntVar()
        Entry(self.win, textvariable=self.salary).place(x=120, y=260)

        # Department ID
        Label(self.win, text="Dep ID").place(x=20, y=300)
        self.dep_id = IntVar()
        Entry(self.win, textvariable=self.dep_id).place(x=120, y=300)

        self.table = ttk.Treeview(self.win, show="headings", columns=[1, 2, 3, 4, 5, 6, 7, 8])
        self.table.place(x=280, y=20, width=580, height=350)

        columns = ["ID", "Name", "Family", "National ID", "Phone", "Position", "Salary", "Dep ID"]
        widths = [40, 70, 70, 90, 90, 75, 70, 55]

        for i, (col, w) in enumerate(zip(columns, widths), start=1):
            self.table.heading(i, text=col)
            self.table.column(i, width=w)

        self.table.bind("<ButtonRelease>", self.table_click)

        Button(self.win, text="Save", command=self.save_click, width=15).place(x=30, y=350)

        self.reset_from()
        
    def reset_from(self):
        self.emp_id.set(0)
        self.name.set("")
        self.family.set("")
        self.national_id.set("")
        self.phone.set("")
        self.position.set("")
        self.salary.set(0)
        self.dep_id.set(0)

        for item in self.table.get_children():
            self.table.delete(item)

        success, data = self.controller.find_all()
        if success:
            for emp in data:
                self.table.insert("", END, values=emp.to_tuple())

        else:
            messagebox.showerror("Load Error", str(data))

    def save_click(self):
        success, message = self.controller.save(
            self.emp_id.get(),
            self.name.get(),
            self.family.get(),
            self.national_id.get(),
            self.phone.get(),
            self.position.get(),
            self.salary.get(),
            self.dep_id.get())

        if success:
            messagebox.showinfo("Success", message)
            self.reset_from()
        else:
            messagebox.showerror("Error", message)

    def table_click(self, event):
        selected = self.table.focus()
        values = self.table.item(selected)["values"]
        if values and len(values) >= 8:
            self.emp_id.set(int(values[0]))
            self.name.set(values[1])
            self.family.set(values[2])
            self.national_id.set(values[3])
            self.phone.set(values[4])
            self.position.set(values[5])
            self.salary.set(int(float(values[6])))
            self.dep_id.set(int(values[7]))