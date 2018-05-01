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
        query = "select * from Participates natural join Groups where uid = %s;"
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