from configs.dbconfig import pg_config
import psycopg2

class AdminDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],

                                                            pg_config['user'],

                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)


    def getAllAdmin(self):
        cursor = self.conn.cursor()
        query = "select * from Administrate;"
        cursor.execute(query)
        result = []

        for row in cursor:
            result.append(row)

        return result

    def getAdminById(self, id):
        cursor = self.conn.cursor()
        query = "select * from Administrate where uid = %s;"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        return result

    def getAdminByUserId(self, uid):
        cursor = self.conn.cursor()
        query = "select * from Administrate where uid = %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdminByGroupId(self, gid):
        cursor = self.conn.cursor()
        query = "select * from Administrate where gid = %s;"
        cursor.execute(query, (gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result