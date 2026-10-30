from tools.validation import Validator


class Employee:
    def __init__(self, emp_id,
                 name, family,
                 national_id,
                 phone_number,
                 position,
                 salary,
                 dep_id):
        self.emp_id = emp_id
        self.name = name
        self.family = family
        self.national_id = national_id
        self.phone_number = phone_number
        self.position = position
        self.salary = salary
        self.dep_id = dep_id



    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        Validator.name_validator(name)
        self.__name = name



    @property
    def family(self):
        return self.__family

    @family.setter
    def family(self, family):
        Validator.family_validator(family)
        self.__family = family



    @property
    def national_id(self):
        return self.__national_id

    @national_id.setter
    def national_id(self, national_id):
        Validator.national_id_validator(national_id)
        self.__national_id = str(national_id)



    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        Validator.phone_number_validator(phone_number)
        self.__phone_number = str(phone_number)



    def __repr__(self):
        return (f"Employee : {self.emp_id:4} "
                f" {self.name:15}"
                f" {self.family:20}"
                f" {self.national_id:15}"
                f" {self.phone_number:14}"
                f" {self.position:20}"
                f" {self.salary:5}"
                f" {self.dep_id:4}")



    def to_tuple(self):
        return (
            self.emp_id,
            self.name,
            self.family,
            self.national_id,
            self.phone_number,
            self.position,
            self.salary,
            self.dep_id
        )