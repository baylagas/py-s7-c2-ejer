from balance_db import (
    insertBalance,
    updateBalance,
    getBalanceById,
    getAllBalance,
    deleteBalance,
)
from prettytable import PrettyTable


def createNewBalance(idUser):
    title = input("title:")
    amount = 0.0
    insertBalance(idUser, title, amount)
    viewAllBalance(idUser)


def modifyBalance(idUser):
    id = int(input("id:"))
    oldBalance = getBalanceById(id)

    print(f"old title: {oldBalance['title']}")
    title = input("new title: ")

    amount = oldBalance["amount"]

    updateBalance(id, idUser, title, amount)
    viewBalanceById(id)


def removeBalance(idUser):
    id = int(input("id:"))
    deleteBalance(id, idUser)
    viewAllBalance()


def viewBalanceById(balanceId):
    balance = getBalanceById(balanceId)
    table = PrettyTable()
    table.field_names = ["id", "idUser", "title", "amount"]
    table.add_row(
        [balance["id"], balance["iduser"], balance["title"], balance["amount"]]
    )
    print(table)
    table.clear()


def viewAllBalance(idUser):
    balanceList = getAllBalance(idUser)

    table = PrettyTable()
    table.field_names = ["id", "iduser", "title", "amount"]

    for balance in balanceList:
        table.add_row(
            [balance["id"], balance["iduser"], balance["title"], balance["amount"]]
        )
    print(table)
    table.clear()


def getBalanceObjectById(idBalance):
    return getBalanceById(idBalance)


# createNewBalance()
# modifyBalance()
# removeBalance()
# viewAllBalance()
# viewBalanceById(1)
