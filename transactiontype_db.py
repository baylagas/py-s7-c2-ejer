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


def getTransactionById(id):
    try:
        connection = getConnection()
        with connection.cursor() as mycursor:
            sql = f"SELECT * FROM pfinancedb.transaction_type where id={id};"
            mycursor.execute(sql)
            user = mycursor.fetchone()
    finally:
        connection.close()
    return user


def getAllTransaction():
    try:
        connection = getConnection()
        with connection.cursor() as mycursor:
            sql = "SELECT * FROM pfinancedb.transaction_type;"
            mycursor.execute(sql)
            user = mycursor.fetchall()
    finally:
        connection.close()
    return user
