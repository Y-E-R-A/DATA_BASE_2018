from configs.dbconfig import pg_config
import psycopg2


class PinDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllPin(self):
        cursor = self.conn.cursor()
        query = "select * from Participates;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPinById(self, id):
        cursor = self.conn.cursor()
        query = "select * from Participates where id = %s;"
        cursor.execute(query, (id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPinByUserId(self, uid):
        cursor = self.conn.cursor()
        query = "select * from Participates where uid = %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPinByGroupId(self, gid):
        cursor = self.conn.cursor()
        query = "select * from Participates where gid = %s;"
        cursor.execute(query, (gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getPinNamesByGroupId(self, gid):
        cursor = self.conn.cursor()
        query = "Select uid, ufirst_name, ulast_name " \
                "From Participates natural inner join Users " \
                "Where gid = %s;"
        cursor.execute(query, (gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self,uid,gid):
        print("PinDAO")
        print(uid)
        print(gid)
        cursor = self.conn.cursor()
        query = "insert into participates (uid, gid) values ( %s, %s) ;"
        cursor.execute(query, (uid, gid,))
        self.conn.commit()
        return