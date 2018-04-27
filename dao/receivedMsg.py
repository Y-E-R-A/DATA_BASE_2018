from configs.dbconfig import pg_config
import psycopg2

class ReceivedMsgDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllReceivedMsg(self):
        cursor = self.conn.cursor()
        query = "select * from Receive;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReceivedMsgById(self, mid):
        cursor = self.conn.cursor()
        query = "select * from Receive where mid = %s;"
        cursor.execute(query, (mid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReceivedMsgByUserId(self, uid):
        cursor = self.conn.cursor()
        query = "select * from Receive where uid = %s;"
        cursor.execute(query, (uid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReceivedMsgByMessageId(self, id):
        cursor = self.conn.cursor()
        query = "select * from Receive where id = %s;"
        cursor.execute(query, (id))
        result = []
        for row in cursor:
            result.append(row)
        return result
