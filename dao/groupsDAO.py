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
        query = "Select gname, Messages.uid, minfo, mdate " \
                "From (Messages INNER JOIN isPart " \
                "ON Messages.mid = isPart.mid) INNER JOIN Groups " \
                "ON Groups.gid = isPart.gid " \
                "Where Groups.gid= %s " \
                "order by mdate desc;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

