from configs.dbconfig import pg_config
import psycopg2

class messageDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllMessages(self):
        cursor = self.conn.cursor()
        query = "select * from Messages;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessageById(self, mid):
        print (mid)
        cursor = self.conn.cursor()
        query = "select * from Messages where mid = %s;"
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessageByDate(self, mdate):
        cursor = self.conn.cursor()
        query = "select * from Messages where mdate = %s;"
        cursor.execute(query, (mdate,))
        result = []
        for row in cursor:
            result.append(row)
        return result

        ##Originally getByBody

    def getMessageByInfo(self, minfo):
        cursor = self.conn.cursor()
        query = "select * from Messages where minfo = %s;"
        cursor.execute(query, (minfo,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllMessageByUserId(self, uid):
        cursor = self.conn.cursor()
        query = "select * from Messages where uid = %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result









    def insert(self, mdate, minfo, uid):
        cursor = self.conn.cursor()
        query = "insert into messages(mdate, minfo, uid) values (%s, %s, %s) returning mid;"
        cursor.execute(query, (mdate, minfo, uid,))
        mid = cursor.fetchone()[0]
        self.conn.commit()
        return mid

    def update(self, uid, mdate, minfo, mid):
        cursor = self.conn.cursor()
        query = "update messages set uid = %s, mdate = %s, minfo = %s where mid = %s;"
        cursor.execute(query, (mid, mdate, minfo, uid,))
        self.conn.commit()
        return mid

