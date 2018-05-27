from configs.dbconfig import pg_config
import psycopg2

class UserDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from Users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getUserById(self, uid):
        cursor = self.conn.cursor()
        query = "select * from Users where uid = %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getUserByName(self, name):
        cursor = self.conn.cursor()
        query = "select * from Users where ufirst_name = %s;"
        cursor.execute(query, (name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByLastname(self, lastname):
        cursor = self.conn.cursor()
        query = "select * from Users where ulast_name = %s;"
        cursor.execute(query, (lastname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByPhone(self, phone):
        # Phone is unique in a user instance
        cursor = self.conn.cursor()
        query = "select * from Users where phone = %s;"
        cursor.execute(query, (phone,))
        result = cursor.fetchone()
        return result

    def getUserByDescription(self, udescription):
        cursor = self.conn.cursor()
        query = "select * from Users where udescription = %s;"
        cursor.execute(query, (udescription,))
        result = cursor.fetchone()
        return result

    def getUserGroupsById(self, uid):
        cursor = self.conn.cursor()
        #query = "select * from Participates natural join Groups where uid = %s;"
        query = "with P as (select * from participates where uid=%s),G as " \
                "(select gid,gname, gdescription,gdCreation,uid as Group_Creator from groups)" \
                "Select *" \
                "from P natural inner join G"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserInformationByUserId(self, uid):
        cursor = self.conn.cursor()
        query = "SELECT cid, uid, ufirst_name, ulast_name, phone, udescription, cusername, cemail " \
                "from Users NATURAL INNER JOIN Credentials Where Users.uid = %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserMessages(self):
        cursor = self.conn.cursor()
        query = "select D.uid,D.mid,D.ufirst_name,D.ulast_name,D.minfo,D.mdate, D.likes, C.dislikes " \
                "from(select A.uid,A.mid,A.ufirst_name,A.ulast_name,A.minfo,A.mdate, B.likes " \
                "from(select u.uid,m.mid,u.ufirst_name,u.ulast_name,m.minfo,m.mdate " \
                "from users as u, messages as m " \
                "where u.uid=m.uid) as A left join (" \
                "select m.mid,count(*) as likes " \
                "from messages as m, reaction as r " \
                "where r.rating='like' " \
                "and m.mid=r.mid " \
                "group by m.mid " \
                ") as B on A.mid=B.mid " \
                ") as D left join (" \
                "select m.mid,count(*) as dislikes " \
                "from messages as m, reaction as r " \
                "where r.rating='dislike' " \
                "and m.mid=r.mid " \
                "group by m.mid) as C on C.mid=D.mid " \
                "order by D.mdate"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self,ufirst_name,ulast_name,udescription):
       # insert
       # into
       # Users(cid, ufirst_name, ulast_name, phone, udescription)
       # values(1, 'Yomaira', 'Rivera', '17875556666', 'Hi everyone');


        #print ("userDAO")
       # cursor = self.conn.cursor()
        #query = "insert into Users()"
        return "Oh Yeah"
