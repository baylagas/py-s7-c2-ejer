import pymysql


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
                + "(`id`,`idbalance`,`idtranstype`,`title`,`amount`) "
                + f"VALUES(0,{idBalance},{idTranstype},'{title}',{amount});"
            )
            mycursor.execute(sql)
            connection.commit()
    finally:
        connection.close()


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


def deleteTransaction(id):
    try:
        connection = getConnection()
        with connection.cursor() as mycursor:
            sql = f"DELETE FROM `pfinancedb`.`transaction` WHERE id={id};"
            mycursor.execute(sql)
            connection.commit()
    finally:
        connection.close()


def getTransactionById(id):
    try:
        connection = getConnection()
        with connection.cursor() as mycursor:
            sql = f"SELECT * FROM pfinancedb.transaction where id={id};"
            mycursor.execute(sql)
            user = mycursor.fetchone()
    finally:
        connection.close()
    return user


def getAllTransaction():
    try:
        connection = getConnection()
        with connection.cursor() as mycursor:
            sql = "SELECT * FROM pfinancedb.transaction;"
            mycursor.execute(sql)
            user = mycursor.fetchall()
    finally:
        connection.close()
    return user
