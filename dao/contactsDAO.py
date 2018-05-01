from configs.dbconfig import pg_config
import psycopg2

class ContactsDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],

                                                            pg_config['user'],

                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)


    def getUserContacts(self, uid):
        cursor = self.conn.cursor()
        query = "Select Contacts.uid, Users.uid AS Contact_ID, Users.ufirst_name AS Contact_firstname," \
                " Users.ulast_name AS Contact_lastname, Credentials.cemail, Users.phone From (Contacts " \
                "inner join Users ON Contacts.cid = Users.uid) inner join Credentials ON Users.cid = Credentials.cid " \
                "Where Contacts.uid = %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserContactByID(self, uid, cid):
        cursor = self.conn.cursor()
        query = "Select Contacts.uid, Users.uid AS Contact_ID, Users.ufirst_name AS Contact_firstname," \
                " Users.ulast_name AS Contact_lastname, Credentials.cemail, Users.phone From (Contacts " \
                "inner join Users ON Contacts.cid = Users.uid) inner join Credentials ON Users.cid = Credentials.cid " \
                "Where Contacts.uid = %s AND Contacts.cid= %s;"
        cursor.execute(query, uid, (cid,))
        result = []
        for row in cursor:
            result.append(row)
        return result