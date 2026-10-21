import re


class Validator:
    @staticmethod
    def name_validator(name):
        if not re.match(r"^[a-zA-Z]{2,30}$", name):
            raise ValueError("Invalid Name")


    @staticmethod
    def family_validator(family):
        if not re.match(r"^[a-zA-Z]{2,30}$", family):
            raise ValueError("Invalid Family")


    @staticmethod
    def national_id_validator(national_id):
        if not re.match(r"^\d{10}$", str(national_id)):
            raise ValueError("Invalid National ID")


    @staticmethod
    def phone_number_validator(phone_number):
        if not re.match(r"^09\d{9}$", str(phone_number)):
            raise ValueError("Invalid Phone Number")