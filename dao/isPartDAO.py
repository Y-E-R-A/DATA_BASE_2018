from configs.dbconfig import pg_config
import psycopg2

class IsPartDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllIsPart(self):
        cursor = self.conn.cursor()
        query = "select * from IsPart;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getIsPartById(self, id):
        cursor = self.conn.cursor()
        query = "select * from IsPart where mid = %s;"
        cursor.execute(query, (id,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getIsPartByMessageId(self, mid):
        cursor = self.conn.cursor()
        query = "select * from IsPart where mid =%s;"
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getIsPartByGroupId(self, id):
        cursor = self.conn.cursor()
        query = "select * from IsPart where gid =%s;"
        cursor.execute(query, (id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, mid, gid):
        cursor = self.conn.cursor()
        query = "insert into IsPart(mid, gid) values (%s, %s);"
        cursor.execute(query, (mid, gid,))
        #mid = cursor.fetchone()[0]
        self.conn.commit()
        return