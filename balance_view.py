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
    viewAllBalance()


def modifyBalance(idUser):
    id = int(input("id:"))
    oldBalance = getBalanceById(id)

    print(f"old title: {oldBalance['title']}")
    title = input("new title: ")

    amount = oldBalance["amount"]

    updateBalance(id, idUser, title, amount)
    viewBalanceById(id)


def removeBalance():
    id = int(input("id:"))
    deleteBalance(id)
    viewAllBalance()


def viewBalanceById(balanceId):
    balance = getBalanceById(balanceId)
    table = PrettyTable()
    table.field_names = ["id", "idUser", "title", "amount"]
    table.add_row(
        [balance["id"], balance["idUser"], balance["title"], balance["amount"]]
    )
    print(table)


def viewAllBalance():
    balanceList = getAllBalance()

    table = PrettyTable()
    table.field_names = ["id", "iduser", "title", "amount"]

    for balance in balanceList:
        table.add_row(
            [balance["id"], balance["iduser"], balance["title"], balance["amount"]]
        )
    print(table)


# createNewBalance()
# modifyBalance()
# removeBalance()
# viewAllBalance()
# viewBalanceById(1)
