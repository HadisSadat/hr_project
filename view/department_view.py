from tkinter import *
from tkinter import ttk, messagebox
from controller.department_controller import DepartmentController


class DepartmentView:
    def __init__(self):
        self.controller = DepartmentController()

        self.win = Toplevel()
        self.win.geometry("600x350")
        self.win.title("Departments")

        # Dep ID
        Label(self.win, text="Dep ID").place(x=20, y=20)
        self.dep_id = IntVar()
        Entry(self.win, textvariable=self.dep_id).place(x=120, y=20)

        # Department Name
        Label(self.win, text="Dep Name").place(x=20, y=60)
        self.department_name = StringVar()
        Entry(self.win, textvariable=self.department_name).place(x=120, y=60)

        # Table
        self.table = ttk.Treeview(self.win, show="headings", columns=[1, 2])
        self.table.place(x=300, y=20, width=280, height=300)

        self.table.column(1, width=80)
        self.table.column(2, width=180)

        self.table.heading(1, text="Dep ID")
        self.table.heading(2, text="Department Name")

        self.table.bind("<ButtonRelease>", self.table_click)

        Button(self.win, text="Save", command=self.save_click, width=15).place(x=30, y=300)
        self.reset_from()

    def reset_from(self):
        self.dep_id.set(0)
        self.department_name.set("")

        for item in self.table.get_children():
            self.table.delete(item)

        success, data = self.controller.find_all()
        if success:
            for dep in data:
                self.table.insert("", END, values=dep.to_tuple())

        else:
            messagebox.showerror("Load Error", str(data))

    def save_click(self):
        success, message = self.controller.save(
            self.dep_id.get(),
            self.department_name.get()
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
            self.dep_id.set(int(values[0]))
            self.department_name.set(values[1])