from configs.dbconfig import pg_config
import psycopg2

class CredentialsDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    def getAllCredentials(self):
        cursor = self.conn.cursor()
        query = "select * from Credentials;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getCredentialsById(self, cid):
        cursor = self.conn.cursor()
        query = "select * from Credentials where cid = %s;"
        cursor.execute(query, (cid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCredentialsByPassword(self, cpassword):
        cursor = self.conn.cursor()
        query = "select * from Credentials where cpassword = %s;"
        cursor.execute(query, (cpassword,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCredentialsByUsername(self, username):
        cursor = self.conn.cursor()
        query = "select * from Credentials where cusername = %s;"
        cursor.execute(query, (username,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCredentialsByEmail(self, email):
        # Email is unique in a user instance
        cursor = self.conn.cursor()
        query = "select * from Credentials where cemail = %s;"
        cursor.execute(query, (email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Does not exist in DB
    def getCredentialsByUserId(self, uid):
        cursor = self.conn.cursor()
        query = "select * from Credentials where uid = %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result