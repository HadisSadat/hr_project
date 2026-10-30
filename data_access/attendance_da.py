from pathlib import Path
import pickle


class AttendanceDa:
    def __init__(self):
        data_dir = Path(__file__).resolve().parent / "data"
        data_dir.mkdir(parents=True, exist_ok=True)
        self.filename = data_dir / "attendance.dat"
        self.attendance_list = self.find_all()



    def save(self, item):
        self.attendance_list = self.find_all()
        self.attendance_list.append(item)
        with self.filename.open("wb") as file:
            pickle.dump(self.attendance_list, file)



    def find_all(self):
        if not self.filename.exists():
            return []
        with self.filename.open("rb") as file:
            return pickle.load(file)