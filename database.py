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


def insertUser(user, password, email, age):
    try:
        connection = getConnection()
        with connection.cursor() as mycursor:
            sql = (
                "INSERT INTO `pfinancedb`.`user`(`id`,`user`,`password`,`email`,`age`) "
                + f"VALUES(0,'{user}','{password}','{email}',{age});"
            )
            mycursor.execute(sql)
            connection.commit()
    finally:
        connection.close()


def updateUser(id, user, password, email, age):
    try:
        connection = getConnection()
        with connection.cursor() as mycursor:
            sql = (
                "UPDATE `pfinancedb`.`user` "
                + f"SET `user` = '{user}',`password` = '{password}',`email` = '{email}',`age` = {age} "
                + f"WHERE `id` = {id};"
            )
            mycursor.execute(sql)
            connection.commit()
    finally:
        connection.close()


def deleteUser(id):
    try:
        connection = getConnection()
        with connection.cursor() as mycursor:
            sql = f"DELETE FROM `pfinancedb`.`user` WHERE id={id};"
            mycursor.execute(sql)
            connection.commit()
    finally:
        connection.close()


def getUserById(id):
    try:
        connection = getConnection()
        with connection.cursor() as mycursor:
            sql = f"SELECT * FROM pfinancedb.user where id={id};"
            mycursor.execute(sql)
            user = mycursor.fetchone()
    finally:
        connection.close()
    return user


def getAllUsers():
    try:
        connection = getConnection()
        with connection.cursor() as mycursor:
            sql = "SELECT * FROM pfinancedb.user;"
            mycursor.execute(sql)
            user = mycursor.fetchall()
    finally:
        connection.close()
    return user
