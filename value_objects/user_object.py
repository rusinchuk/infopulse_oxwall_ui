from datetime import datetime


class User:
    def __init__(self, id=None, username="", password="", real_name="", email="", gender=None, birthday=None, is_admin=False):
        self.id = id
        self.username = username
        self.password = password
        self.real_name = real_name
        self.email = email
        self.gender = gender
        self.birthday = datetime.strptime(birthday, "%Y-%m-%d") if (birthday is not None) else None
        self.is_admin = is_admin

    def __str__(self):
        return f"{self.__class__} object: username={self.username}, real_name={self.real_name}"

    def __repr__(self):
        return f"User(username='{self.username}', password='{self.password}', real_name='{self.real_name}')"

    # def __lt__(self, other):
    #     return self.birthday < other.birthday

    def __eq__(self, other):
        if self.email != "":
            return self.username == other.username and self.real_name == other.real_name and self.email == self.email
        return self.username == other.username and self.real_name == other.real_name


if __name__ == "__main__":
    u1 = User(username="A", birthday="1986-01-16")
    u2 = User(username="A")
    print(repr(u1))
