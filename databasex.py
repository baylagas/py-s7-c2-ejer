import pymysql

"""
el proposito de esta clase va a ser conexion y
execucion de comandos de sql a mysql

def getConnection():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        passwd="12345",
        db="pfinancedb",
        cursorclass=pymysql.cursors.DictCursor,
    )
    return connection

"""


class DatabaseX:
    # crear el constructor de la clase
    def __init__(self):
        self.host = "localhost"  # variables de instancia
        self.user = "root"
        self.password = "12345"
        self.database = "pfinancedb"
        self.cursorClass = pymysql.cursors.DictCursor
        self.connection = self.createConnection()

    def createConnection(self):
        connection = pymysql.connect(
            host=self.host,
            user=self.user,
            passwd=self.password,
            db=self.database,
            cursorclass=self.cursorClass,
        )
        return connection


datab = DatabaseX()
con = datab.connection
mycursor = con.cursor()
mycursor.execute("select * from transaction;")
transList = mycursor.fetchall()
for trans in transList:
    print(trans)
