from configs.dbconfig import pg_config
import psycopg2

class mediaDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllMedia(self):
        cursor = self.conn.cursor()
        query = "select * from Media;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMediaByID(self, meid):
        cursor = self.conn.cursor()
        query = "select * from Media where meid = %s;"
        cursor.execute(query, (meid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMediaByName(self, mename):
        cursor = self.conn.cursor()
        query = "select * from Media where mename = %s;"
        cursor.execute(query, (mename,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMediaByAddress(self, meaddress):
        cursor = self.conn.cursor()
        query = "select * from Media where meaddress = %s;"
        cursor.execute(query, (meaddress,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMediaByType(self, metype):
        cursor = self.conn.cursor()
        query = "select * from Media where metype = %s;"
        cursor.execute(query, (metype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getByMessageId(self, mid):
        cursor = self.conn.cursor()
        query = "select * from Media where mid = %s;"
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result



