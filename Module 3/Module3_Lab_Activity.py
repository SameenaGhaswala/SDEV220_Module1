class Person:
    def __init__(self, first_name, last_name, gender, birth_date, height):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.birth_date = birth_date
        self.height = height

    def info(self):
        print(f"Full name: {self.first_name} {self.last_name}\nBirth date: {self.birth_date}\nGender: {self.gender}\
\nHeight: {self.height}")

    def age_checker(self):
        birth_year = int(self.birth_date[4:8])
        birth_month = int(self.birth_date[0:2])
        birth_day = int(self.birth_date[2:4])
        age = 2026 - birth_year

        if birth_month > 9 or (birth_month == 9 and birth_day > 29):
            age -= 1

        if age < 21:
            print("The person is under 21 years old")
        else:
            print("The person is 21 or over")

for i in range(3):
    try:
        in_first_name = input("Enter your first name: ")
        in_last_name = input("Enter your last name: ")
        in_gender = input("Enter your gender: ")
        in_birth_date = input("Enter your birth date (mmddyyy) format: ")
        in_height = input("Enter your height (in in): ")
        p = Person(in_first_name, in_last_name, in_gender, in_birth_date, in_height)
        p.info()
        p.age_checker()
    except ValueError:
        print("Please enter valid birth date.")

