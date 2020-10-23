from user_db import insertUser, updateUser, getUserById, getAllUsers, deleteUser
from prettytable import PrettyTable


def createNewUser():
    user = "test"
    password = "12345"
    email = "test@hotmail.com"
    age = 23
    insertUser(user, password, email, age)


def modifyUser():
    oldUser = getUserById(3)
    user = oldUser["user"] + "m"
    password = oldUser["password"] + "6"
    email = oldUser["email"] + "x"
    age = int(oldUser["age"]) + 1
    updateUser(3, user, password, email, age)


def removeUser():
    id = 1
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


def viewUserById():
    userId = 1
    user = getUserById(userId)
    table = PrettyTable()
    table.field_names = ["id", "user", "password", "email", "age"]
    table.add_row(
        [user["id"], user["user"], user["password"], user["email"], user["age"]]
    )
    print(table)


# createNewUser()
# modifyUser()
# viewAllUsers()
viewUserById()
