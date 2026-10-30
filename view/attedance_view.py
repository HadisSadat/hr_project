from tkinter import *
from tkinter import ttk, messagebox
from controller.attendance_controller import AttendanceController


class AttendanceView:
    def __init__(self):
        self.controller = AttendanceController()

        self.win = Toplevel()
        self.win.geometry("750x350")
        self.win.title("Attendance")

        # Attendance ID
        Label(self.win, text="Att ID").place(x=20, y=20)
        self.att_id = IntVar()
        Entry(self.win, textvariable=self.att_id).place(x=120, y=20)

        # Employee ID
        Label(self.win, text="Emp ID").place(x=20, y=60)
        self.emp_id = IntVar()
        Entry(self.win, textvariable=self.emp_id).place(x=120, y=60)

        # Date
        Label(self.win, text="Date").place(x=20, y=100)
        self.date = StringVar()
        # فرمت : YYYY-MM-DD
        Entry(self.win, textvariable=self.date).place(x=120, y=100)
        Label(self.win, text="(YYYY-MM-DD)", font=("Arial", 8)).place(x=270, y=102)

        # Check In
        Label(self.win, text="Check In").place(x=20, y=140)
        self.check_in = StringVar()
        # فرمت : HH:MM
        Entry(self.win, textvariable=self.check_in).place(x=120, y=140)
        Label(self.win, text="(HH:MM)", font=("Arial", 8)).place(x=270, y=142)

        # Check Out
        Label(self.win, text="Check Out").place(x=20, y=180)
        self.check_out = StringVar()
        Entry(self.win, textvariable=self.check_out).place(x=120, y=180)

        # Table
        self.table = ttk.Treeview(self.win, show="headings", columns=[1, 2, 3, 4, 5, 6])
        self.table.place(x=360, y=20, width=390, height=300)

        self.table.column(1, width=50)
        self.table.column(2, width=50)
        self.table.column(3, width=80)
        self.table.column(4, width=60)
        self.table.column(5, width=60)
        self.table.column(6, width=60)

        self.table.heading(1, text="Att ID")
        self.table.heading(2, text="Emp ID")
        self.table.heading(3, text="Date")
        self.table.heading(4, text="Check In")
        self.table.heading(5, text="Check Out")
        self.table.heading(6, text="Hours")

        self.table.bind("<ButtonRelease>", self.table_click)

        Button(self.win, text="Save", command=self.save_click, width=15).place(x=30, y=300)
        self.reset_from()

    def reset_from(self):
        self.att_id.set(0)
        self.emp_id.set(0)
        self.date.set("")
        self.check_in.set("")
        self.check_out.set("")

        for item in self.table.get_children():
            self.table.delete(item)

        success, data = self.controller.find_all()
        if success:
            for att in data:
                self.table.insert("", END, values=att.to_tuple())

        else:
            messagebox.showerror("Load Error", str(data))

    def save_click(self):
        success, message = self.controller.save(
            self.att_id.get(),
            self.emp_id.get(),
            self.date.get(),
            self.check_in.get(),
            self.check_out.get()
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
            self.att_id.set(int(values[0]))
            self.emp_id.set(int(values[1]))
            self.date.set(values[2])
            self.check_in.set(values[3])
            self.check_out.set(values[4])