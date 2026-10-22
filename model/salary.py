from tools.validation import Validator


class Salary:
    def __init__(self, salary_id, emp_id, base_salary, overtime, bonus):
        self.salary_id = salary_id
        self.emp_id = emp_id
        self.base_salary = base_salary
        self.overtime = overtime
        self.bonus = bonus

    def calculate_total(self):
        Validator.positive_number_validator(self.base_salary)
        Validator.positive_number_validator(self.overtime)
        Validator.positive_number_validator(self.bonus)

        total = self.base_salary + (self.overtime * 50000) + self.bonus
        return total

    def to_tuple(self):
        return (self.salary_id, self.emp_id, self.base_salary, self.overtime, self.bonus, self.calculate_total())