from transaction_db import (
    insertTransaction,
    updateTransaction,
    getTransactionById,
    getAllTransaction,
    deleteTransaction,
)
from prettytable import PrettyTable


def createNewTransaction(idBalance, idTranstype):
    title = input("title: ")
    amount = float(input("amount: "))
    insertTransaction(idBalance, idTranstype, title, amount)
    viewAllTransaction()


def modifyTransaction(idBalance, idTranstype):
    id = int(input("id:"))
    oldBalance = getBalanceById(id)

    print(f"old title: {oldBalance['title']}")
    title = input("new title: ")

    amount = oldBalance["amount"]

    updateBalance(id, idUser, title, amount)
    viewBalanceById(id)


def viewAllTransaction(idBalance):
    transactionList = getAllTransaction(idBalance)

    table = PrettyTable()
    table.field_names = ["id", "idbalance", "idtranstype", "title", "amount", "created"]

    for transaction in transactionList:
        table.add_row(
            [
                transaction["id"],
                transaction["idbalance"],
                transaction["idtranstype"],
                transaction["title"],
                transaction["amount"],
                transaction["created"],
            ]
        )
    print(table)
