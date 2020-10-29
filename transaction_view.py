from transaction_db import (
    insertTransaction,
    updateTransaction,
    getTransactionById,
    getAllTransaction,
    deleteTransaction,
)
from prettytable import PrettyTable


def createNewTransaction(idBalance):
    idTranstype = int(input("transaction type (1 - income, 2 - expense): "))
    title = input("title: ")
    amount = float(input("amount: "))
    insertTransaction(idBalance, idTranstype, title, amount)
    viewAllTransaction(idBalance)


def modifyTransaction(idBalance):
    id = int(input("id:"))
    oldTransaction = getTransactionById(id, idBalance)

    print(f"old transaction type: {oldTransaction['idtranstype']}")
    idTranstype = input("new transaction type (1-Income, 2-Expense): ")

    print(f"old title: {oldTransaction['title']}")
    title = input("new title: ")

    print(f"old amount: {oldTransaction['amount']}")
    amount = float(input("new amount: "))

    updateTransaction(id, idBalance, idTranstype, title, amount)
    viewTransactionById(id, idBalance)


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


def viewTransactionById(idTransaction, idBalance):
    transaction = getTransactionById(idTransaction, idBalance)
    table = PrettyTable()
    table.field_names = ["id", "idbalance", "idtranstype", "title", "amount", "created"]
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
    table.clear()
