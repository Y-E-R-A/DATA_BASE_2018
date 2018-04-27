from configs.dbconfig import pg_config
import psycopg2


class ReactionDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllReactions(self):
        cursor = self.conn.cursor()
        query = "select * from Reaction;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getByReactionId(self, rid):
        cursor = self.conn.cursor()
        query = "select * from Reaction where rid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getByMessageID(self, mid):
        cursor = self.conn.cursor()
        query = "select * from Reaction where mid = %s;"
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getByUserId(self, uid):
        cursor = self.conn.cursor()
        query = "select * from Reaction where uid = %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getByLikeDislike(self, rating):
        cursor = self.conn.cursor()
        query = "select * from Reaction where rating = %s;"
        cursor.execute(query, (rating,))
        result = []
        for row in cursor:
            result.append(row)
        return result


