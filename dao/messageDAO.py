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


    def getConversation(self, uid1, uid2):
        cursor = self.conn.cursor()
        query = "select M.mid,mdate,minfo,M.uid as sender, R.uid as receiver " \
                "from messages as M inner join receive as R on R.mid = M.mid " \
                "where (M.uid= %s and R.uid = %s) or (M.uid = %s and R.uid = %s) " \
                "order by mdate desc;"
        cursor.execute(query, (uid1, uid2, uid2, uid1))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getHashtagMessages(self, gid):
        cursor = self.conn.cursor()
        query = "with    messages_in_group as (Select G.gid, gname, M.mid, minfo, mdate, U.uid, cusername " \
                "From (Messages as M INNER JOIN isPart " \
                "ON M.mid = isPart.mid) INNER JOIN Groups as G " \
                "ON G.gid = isPart.gid INNER JOIN users as U " \
                "ON M.uid = U.uid INNER JOIN credentials as C " \
                "ON C.cid = U.cid " \
                "Where G.gid= %s), " \
                "messages_likes as (select m.mid,count(*) as likes " \
                "from messages as m, reaction as r " \
                "where r.rating='like' and m.mid=r.mid " \
                "group by m.mid), " \
                "messages_dislikes as (select m.mid,count(*) as dislikes " \
                "from messages as m, reaction as r " \
                "where r.rating='dislike' and m.mid=r.mid " \
                "group by m.mid) " \
                "select gid, gname, M.mid, minfo, mdate, uid, cusername, L.likes, D.dislikes " \
                "from messages_in_group as M left join messages_likes as L on M.mid = L.mid " \
                "left join messages_dislikes as D on M.mid = D.mid " \
                "where minfo like '#%';"
        cursor.execute(query, (gid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result



    def insert(self, mdate, minfo, uid):
        cursor = self.conn.cursor()
        query = "insert into messages(mdate, minfo, uid) values (now(), %s, %s) returning mid;"
        cursor.execute(query, (minfo, uid,))
        mid = cursor.fetchone()[0]
        self.conn.commit()
        return mid

    def update(self, uid, mdate, minfo, mid):
        cursor = self.conn.cursor()
        query = "update messages set uid = %s, mdate = %s, minfo = %s where mid = %s;"
        cursor.execute(query, (mid, mdate, minfo, uid,))
        self.conn.commit()
        return mid



