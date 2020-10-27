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


def insertBalance(idUser, title, amount=0.0):
    try:
        connection = getConnection()
        with connection.cursor() as mycursor:
            sql = (
                f"INSERT INTO `pfinancedb`.`balance` (`id`,`iduser`,`title`,`amount`) "
                + f"VALUES(0,{idUser},'{title}',{amount});"
            )
            mycursor.execute(sql)
            connection.commit()
    finally:
        connection.close()


def updateBalance(id, idUser, title, amount):
    try:
        connection = getConnection()
        with connection.cursor() as mycursor:
            sql = (
                "UPDATE `pfinancedb`.`balance` "
                + f"SET `iduser` = {idUser},`title` = '{title}',`amount` = {amount} "
                + f"WHERE `id` = {id};"
            )
            mycursor.execute(sql)
            connection.commit()
    finally:
        connection.close()


def deleteBalance(id):
    try:
        connection = getConnection()
        with connection.cursor() as mycursor:
            sql = f"DELETE FROM `pfinancedb`.`balance` WHERE id={id};"
            mycursor.execute(sql)
            connection.commit()
    finally:
        connection.close()


def getBalanceById(id):
    try:
        connection = getConnection()
        with connection.cursor() as mycursor:
            sql = f"SELECT * FROM pfinancedb.balance where id={id};"
            mycursor.execute(sql)
            user = mycursor.fetchone()
    finally:
        connection.close()
    return user


def getAllBalance():
    try:
        connection = getConnection()
        with connection.cursor() as mycursor:
            sql = "SELECT * FROM pfinancedb.balance;"
            mycursor.execute(sql)
            user = mycursor.fetchall()
    finally:
        connection.close()
    return user
