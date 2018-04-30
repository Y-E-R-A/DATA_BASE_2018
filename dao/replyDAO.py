from configs.dbconfig import pg_config
import psycopg2

class ReplyDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllReply(self):
        cursor = self.conn.cursor()
        query = "select * from Reply;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReplyById(self, id):
        cursor = self.conn.cursor()
        query = "select * from reply where id = %s;"
        cursor.execute(query, (id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReplyByMessageId(self, mid):
        cursor = self.conn.cursor()
        query = "select * from reply where mid = %s;"
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReplyByReplyToId(self, rid):
        cursor = self.conn.cursor()
        query = "select * from reply where rid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

