from datetime import datetime

class Attendance:
    def __init__(self, att_id, emp_id, date, check_in, check_out):
        self.att_id = att_id
        self.emp_id = emp_id
        self.date = date
        self.check_in = check_in
        self.check_out = check_out

    def calculate_hour(self):
        try:
            fmt = '%H:%M'
            t1 = datetime.strptime(self.check_in, fmt)
            t2 = datetime.strptime(self.check_out, fmt)
        except (ValueError, TypeError):
            raise ValueError("Time format must be HH:MM")

        if t2 < t1:
            raise ValueError("Check-out time cannot be before Check-in time")

        return (t2 - t1).total_seconds() / 3600.0


    def __repr__(self):
        return (f"Attendance : {self.att_id:4}"
                f" {self.emp_id:4}"
                f" {self.date:10}"
                f" {self.check_in:5}"
                f" {self.check_out:5}")


    def to_tuple(self):
        return (self.att_id,
                self.emp_id,
                self.date,
                self.check_in,
                self.check_out,
                round(self.calculate_hour(), 2)
                )