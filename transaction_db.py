import pymysql


INCOME = 1
EXPENSE = 2


def getConnection():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        passwd="12345",
        db="pfinancedb",
        cursorclass=pymysql.cursors.DictCursor,
    )
    return connection


def insertTransaction(idBalance, idTranstype, title, amount=0.0):
    try:
        connection = getConnection()
        with connection.cursor() as mycursor:
            sql = (
                "INSERT INTO `pfinancedb`.`transaction` "
                + "(`id`,`idbalance`,`idtranstype`,`title`,`amount`,created) "
                + f"VALUES(0,{idBalance},{idTranstype},'{title}',{amount},NOW());"
            )
            print(sql)
            mycursor.execute(sql)
            connection.commit()
    finally:
        connection.close()
        recalculateBalance(idBalance)


def updateTransaction(id, idBalance, idTranstype, title, amount=0.0):
    try:
        connection = getConnection()
        with connection.cursor() as mycursor:
            sql = (
                "UPDATE `pfinancedb`.`transaction` "
                + f"SET `idbalance` = {idBalance},`idtranstype` = {idTranstype}, "
                + f"`title` = '{title}',`amount` = {amount},`created` = NOW() "
                + f"WHERE `id` = {id};"
            )
            mycursor.execute(sql)
            connection.commit()
    finally:
        connection.close()
        recalculateBalance(idBalance)


def deleteTransaction(id):
    try:
        connection = getConnection()
        with connection.cursor() as mycursor:
            sql = f"DELETE FROM `pfinancedb`.`transaction` WHERE id={id};"
            mycursor.execute(sql)
            connection.commit()
    finally:
        connection.close()


def getTransactionById(id, idBalance):
    try:
        connection = getConnection()
        with connection.cursor() as mycursor:
            sql = (
                f"SELECT * FROM pfinancedb.transaction "
                + f"where id={id} and idbalance={idBalance};"
            )
            mycursor.execute(sql)
            user = mycursor.fetchone()
    finally:
        connection.close()
    return user


def getAllTransaction(idBalance):
    try:
        connection = getConnection()
        with connection.cursor() as mycursor:
            sql = (
                f"SELECT * FROM pfinancedb.transaction "
                + f"where idbalance={idBalance};"
            )
            mycursor.execute(sql)
            user = mycursor.fetchall()
    finally:
        connection.close()
    return user


def getTotalTrans(idBalance, idTranstype):
    try:
        connection = getConnection()
        with connection.cursor() as mycursor:
            sql = (
                "select if(sum(amount) is null, 0.0, sum(amount)) as total "
                + f"from pfinancedb.transaction where idbalance={idBalance} and idtranstype={idTranstype};"
            )
            mycursor.execute(sql)
            totalIncome = mycursor.fetchone()
    finally:
        connection.close()
    return totalIncome


def recalculateBalance(idBalance):
    totalIncome = getTotalTrans(idBalance, INCOME)
    totalExpense = getTotalTrans(idBalance, EXPENSE)
    totalBalance = totalIncome["total"] - totalExpense["total"]
    try:
        connection = getConnection()
        with connection.cursor() as mycursor:
            sql = (
                "UPDATE `pfinancedb`.`balance` "
                + f"SET `amount` = {totalBalance} WHERE `id` = {idBalance};"
            )
            mycursor.execute(sql)
            connection.commit()
    finally:
        connection.close()
