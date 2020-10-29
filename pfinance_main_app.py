from user_view import (
    viewAllUsers,
    createNewUser,
    modifyUser,
    removeUser,
    getUserObjectById,
)
from balance_view import (
    viewAllBalance,
    createNewBalance,
    modifyBalance,
    removeBalance,
    getBalanceObjectById,
)
from transaction_view import viewAllTransaction, createNewTransaction, modifyTransaction


def goToBalanceSubMenu(userObj):
    idBalance = int(input("id balance: "))
    # currentBalance = getBalanceObjectById(idBalance)
    while True:
        currentBalance = getBalanceObjectById(idBalance)
        print(
            f"balance: {userObj['user']}|{currentBalance['title']}"
            + f"|${currentBalance['amount']:.2f} - submenu"
        )
        print("0 - back to balance")
        print("1 - view all transaction")
        print("2 - create transaction")
        print("3 - modify transaction")
        print("4 - delete transaction")
        option = int(input("option: "))

        if option == 0:
            print("back to balance...")
            break
        elif option == 1:
            viewAllTransaction(idBalance)
        elif option == 2:
            createNewTransaction(idBalance)
        elif option == 3:
            modifyTransaction(idBalance)


def goToUserSubMenu():
    idUser = int(input("id User: "))
    currentUser = getUserObjectById(idUser)
    while True:
        print(f"user: {currentUser['user']} - submenu")
        print("0 - back to users")
        print("1 - view all balance")
        print("2 - create balance")
        print("3 - modify balance")
        print("4 - delete balance")
        print("5 - go to balance submenus")
        option = int(input("option: "))

        if option == 0:
            print("back to users...")
            break
        elif option == 1:
            viewAllBalance(idUser)
        elif option == 2:
            createNewBalance(idUser)
        elif option == 3:
            modifyBalance(idUser)
        elif option == 4:
            removeBalance(idUser)
        elif option == 5:
            goToBalanceSubMenu(currentUser)


while True:
    print("pfinance...")
    print("0 - exit")
    print("1 - view all users")
    print("2 - create user")
    print("3 - modify user")
    print("4 - delete user")
    print("5 - go to user submenus")
    option = int(input("option: "))

    if option == 0:
        print("pfinance exit...")
        break
    elif option == 1:
        viewAllUsers()
    elif option == 2:
        createNewUser()
    elif option == 3:
        modifyUser()
    elif option == 4:
        removeUser()
    elif option == 5:
        goToUserSubMenu()
