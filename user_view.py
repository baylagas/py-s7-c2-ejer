from user_db import insertUser, updateUser, getUserById, getAllUsers, deleteUser
from prettytable import PrettyTable


def createNewUser():
    user = input("user:")
    password = input("password:")
    email = input("email:")
    age = int(input("email:"))
    insertUser(user, password, email, age)
    viewAllUsers()


def modifyUser():
    id = int(input("id:"))
    oldUser = getUserById(id)

    print(f"old user: {oldUser['user']}")
    user = input("new user: ")

    print(f"old password: {oldUser['password']}")
    password = input("new password: ")

    print(f"old email: {oldUser['email']}")
    email = input("new email: ")

    print(f"old age: {oldUser['age']}")
    age = int(input("new age: "))

    updateUser(id, user, password, email, age)
    viewUserById(id)


def removeUser():
    id = int(input("id:"))
    deleteUser(id)
    viewAllUsers()


def viewAllUsers():
    userList = getAllUsers()

    table = PrettyTable()
    table.field_names = ["id", "user", "password", "email", "age"]

    for user in userList:
        table.add_row(
            [user["id"], user["user"], user["password"], user["email"], user["age"]]
        )
    print(table)


def viewUserById(userId):
    user = getUserById(userId)
    table = PrettyTable()
    table.field_names = ["id", "user", "password", "email", "age"]
    table.add_row(
        [user["id"], user["user"], user["password"], user["email"], user["age"]]
    )
    print(table)


# createNewUser()
# modifyUser()
# removeUser()
# viewAllUsers()
# viewUserById(1)
