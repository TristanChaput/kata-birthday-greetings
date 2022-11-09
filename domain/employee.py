class Employee:
    def __init__(self, last_name, first_name, date_of_birth, email):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.email = email

    def __eq__(self, other) -> bool:
        if isinstance(other, Employee):
            return (
                self.last_name == other.last_name
                and self.first_name == other.first_name
                and self.date_of_birth == other.date_of_birth
                and self.email == other.email
            )
        return False
