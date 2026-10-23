import os
import pickle


class AttendanceDa:
    def __init__(self):
        self.filename = "data_access/data/attendance.dat"
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        self.attendance_list = self.find_all()

    def save(self, attendance):
        self.attendance_list.append(attendance)
        file = open(self.filename, "wb")
        pickle.dump(self.attendance_list, file)
        file.close()

    def find_all(self):
         if not os.path.exists(self.filename):
            return []
         else:
            file = open(self.filename, "rb")
            attendance_list = pickle.load(file)
            file.close()
            return attendance_list