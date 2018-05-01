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

    def getLikesOfMessageById(self, mid):
        cursor = self.conn.cursor()
        query = "SELECT Messages.mid, Messages.minfo, count(*) from MESSAGES INNER JOIN REACTION ON " \
                "MESSAGES.MID= REACTION.MID GROUP BY Messages.mid, Reaction.Rating HAVING " \
                "Reaction.Rating='like' AND Messages.mid = %s;"
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPeopleWhoLikesMessageId(self, mid):
        cursor = self.conn.cursor()
        query = "SELECT Messages.mid, Messages.minfo, Users.uid, Users.ufirst_name, Users.ulast_name from (MESSAGES INNER JOIN REACTION ON" \
                " Messages.mid= reaction.mid)  INNER JOIN USERS ON Reaction.uid= Users.uid WHERE " \
                "Reaction.Rating='like' AND Messages.mid = %s;"
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getDislikesByMessageId(self, mid):
        cursor = self.conn.cursor()
        query = "SELECT Messages.mid, Messages.minfo, count(*) from MESSAGES INNER JOIN REACTION ON  " \
                "Messages.mid= reaction.mid GROUP BY Messages.mid, Reaction.Rating Having " \
                "Reaction.Rating='dislike' AND Messages.mid = %s;"
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPeopleWhoDislikesMessageId(self, mid):
        cursor = self.conn.cursor()
        query = "SELECT Messages.mid, Messages.minfo, Users.uid, Users.ufirst_name, Users.ulast_name from (MESSAGES INNER JOIN REACTION ON" \
                " Messages.mid= reaction.mid)  INNER JOIN USERS ON Reaction.uid= Users.uid WHERE " \
                "Reaction.Rating='dislike' AND Messages.mid = %s;"
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







    def insert(self, mid, uid, rating):
        cursor = self.conn.cursor()
        query = "insert into Reaction(mid, uid, rating) values (%s, %s, %s) returning rid;"
        cursor.execute(query, (mid, uid, rating,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid

    def update(self, mid, uid, rating):
        cursor = self.conn.cursor()
        query = "update Reaction set mid = %s, uid = %s, rating = %s where mid = %s;"
        cursor.execute(query, (mid, uid, rating,))
        self.conn.commit()
        return mid