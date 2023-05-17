from datetime import datetime as dt

import psycopg2


def fetch_data():
    conn = None
    try:
        # Connect to your postgres DB
        conn = psycopg2.connect("dbname=somisettyv user=postgres")
        cur = conn.cursor()
        cur.execute("SELECT * FROM accounts")
        records = cur.fetchall()
        print(records)
        return records
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_vendor_list(account_list):
    """ insert multiple accounts into the vendors table  """
    sql = "INSERT INTO accounts(user_id, username, password, email, created_on, last_login ) VALUES(%s, %s, %s, %s, " \
          "%s, %s)"
    conn1 = None
    try:
        conn1 = psycopg2.connect("dbname=somisettyv user=postgres")
        # create a new cursor
        cur1 = conn1.cursor()
        # execute the INSERT statement
        cur1.executemany(sql, account_list)
        # commit the changes to the database
        conn1.commit()
        # close communication with the database
        cur1.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn1 is not None:
            conn1.close()


class Account:
    def __init__(self, user_id, username, password, email, created_on, last_login):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.created_on = created_on
        self.last_login = last_login


if __name__ == '__main__':
    fetch_data()
    a1 = Account(5, 'test1', 'test1', 'test1', dt.now(), dt.now())

    insert_vendor_list(
        [(5, 'test2', 'test2', 'test2', dt.now(), dt.now())]
    )


