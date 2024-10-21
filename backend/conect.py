import pymysql

conexion = pymysql.connect(host = 'localhost', user = 'root', passwd = '123456', db = 'products-tech')

cur = conexion.cursor()
cur.execute("select Id_usuario, nombre_completo, nick, email, contrasena from users")
for Id_usuario, nombre_completo,nick, email, contrasena in cur.fetchall():
    print(Id_usuario, " | ", nombre_completo)

conexion.close()
