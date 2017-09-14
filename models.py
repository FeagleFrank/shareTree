import pymysql
from settings import mysqlConfig


class Conn(object):
    _conn = None
    _cursor = None

    @staticmethod
    def create_conn():
        Conn._conn = pymysql.connect(**mysqlConfig)
        Conn._cursor = Conn._conn.cursor()

    @staticmethod
    def query_sql(sql, param=None):
        Conn.create_conn()
        Conn._cursor.execute(sql, param)
        result = Conn._cursor.fetchall()
        Conn._cursor.close()
        Conn._conn.close()
        return result

    @staticmethod
    def query_one_sql(sql, param=None):
        Conn.create_conn()
        Conn._cursor.execute(sql, param)
        result = Conn._cursor.fetchone()
        Conn._cursor.close()
        Conn._conn.close()
        return result

    @staticmethod
    def exec_sql(sql, param=None):
        Conn.create_conn()
        Conn._cursor.execute(sql, param)
        Conn._conn.commit()
        Conn._cursor.close()
        Conn._conn.close()