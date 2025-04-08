from faker import Faker


class UserData:
    def __init__(self):
        __faker = Faker('en-us')
        self.first_name: str = __faker.name()
        self.last_name: str = __faker.last_name()
        self.username: str = '_'.join([self.first_name, self.last_name, __faker.user_name()]).replace(' ', '_').lower()
        self.email: str = '_'.join([self.username, __faker.email()]).replace(' ', '_').lower()
        self.password: str = __faker.password()
