from configs.dbconfig import pg_config
import psycopg2


class groupDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllGroups(self):
        cursor = self.conn.cursor()
        query = "Select * from Groups;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupsById(self, gid):
        cursor = self.conn.cursor()
        query = "select * from Groups where gid = %s;"
        cursor.execute(query, (gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Select Users.ufirst_name, Users.ulast_name from Users, Participates where Users.uid = Participates.uid and Participates.gid = 2
    def getGroupsByName(self, groupname):
        cursor = self.conn.cursor()
        query = "Select * from Groups where gname = %s;"
        cursor.execute(query, (groupname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupsByDescription(self, gdescription):
        cursor = self.conn.cursor()
        query = "Select * from Groups where gdescription = %s;"
        cursor.execute(query, (gdescription,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupByCreation(self, gdate):
        cursor = self.conn.cursor()
        query = "Select * from Groups where gdcreation = %s;"
        cursor.execute(query, (gdate,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getByUserId(self, uid):
        cursor = self.conn.cursor()
        query = "Select * from Groups where uid = %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessagesByGroupId(self, gid):
        cursor = self.conn.cursor()
        #query = "Select G.gid, M.mid, minfo, mdate, U.uid, cusername " \
        #        "from (Messages as M inner join isPart ON M.mid=isPart.mid) " \
        #        "inner join Groups as G ON G.gid = isPart.gid inner join users as U " \
        #        "ON M.uid = U.uid inner join credentials as C " \
        #        "ON C.cid = U.cid " \
        #        "Where G.gid = 1 " \
        #        "order by mdate desc;"
        query = "select D.gid, D.gname, D.mid, D.minfo, D.mdate, D.uid, D.cusername, D.likes, C.dislikes " \
                "from    (select A.gid, A.gname, A.mid, A.minfo, A.mdate, A.uid, A.cusername, B.likes " \
                "from(Select G.gid, gname, M.mid, minfo, mdate, U.uid, cusername " \
                "From (Messages as M INNER JOIN isPart " \
                "ON M.mid = isPart.mid) INNER JOIN Groups as G " \
                "ON G.gid = isPart.gid INNER JOIN users as U " \
                "ON M.uid = U.uid INNER JOIN credentials as C " \
                "ON C.cid = U.cid " \
                "Where G.gid= %s ) as A left join (" \
                "select m.mid,count(*) as likes " \
                "from messages as m, reaction as r " \
                "where r.rating='like' and m.mid=r.mid " \
                "group by m.mid) as B on A.mid=B.mid) as D left join ( " \
                "select m.mid,count(*) as dislikes " \
                "from messages as m, reaction as r " \
                "where r.rating='dislike' and m.mid=r.mid " \
                "group by m.mid) as C on C.mid=D.mid " \
                "order by D.mdate;"
        cursor.execute(query, (gid,))
        result = []
        ##query = "Select gname, minfo, Messages.uid From (Messages INNER JOIN isPart " \
        #        "ON Messages.mid = isPart.mid) INNER JOIN Groups ON Groups.gid = isPart.gid" \
        #        " Where Groups.gid= %s;"
        for row in cursor:
            result.append(row)
        return result
