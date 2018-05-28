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

#Select Users.ufirst_name, Users.ulast_name from Users, Participates where Users.uid = Participates.uid and Participates.gid = 2
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

    def getMessagesByGroupId(self, uid):
        cursor = self.conn.cursor()
        query = "Select gname, minfo, Messages.uid From (Messages INNER JOIN isPart " \
                "ON Messages.mid = isPart.mid) INNER JOIN Groups ON Groups.gid = isPart.gid" \
                " Where Groups.gid= %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self,gname,gdescription, gcreation, adminId):
        print ("GroupDAO")
        print(gname)
        print(gdescription)
        print("gcreation ",gcreation)
        print("admin Id: ", adminId)
        cursor = self.conn.cursor()
        query = "insert into Groups(gname, gdescription, gdcreation, uid) values ( %s, %s, now(), %s) returning gid;"
        cursor.execute(query, (gname, gdescription, adminId,))
        gid = cursor.fetchone()[0]
        self.conn.commit()
        return gid