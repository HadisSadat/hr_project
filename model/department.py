from tools.validation import Validator


class Department:
    def __init__(self, dep_id, department_name):
        self.dep_id = dep_id
        self.department_name = department_name

    @property
    def department_name(self):
        return self.__department_name

    @department_name.setter
    def department_name(self, name):
        Validator.name_validator(name)
        self.__department_name = name

    def __repr__(self):
        return f"Department({self.dep_id:4}, {self.department_name:8})"

    def to_tuple(self):
        return self.dep_id, self.department_name