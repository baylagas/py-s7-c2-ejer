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


def viewAllTransaction():
    transactionList = getAllTransaction()

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
