import pymysql


class MariaDB:
    def __init__(self, data):
        self.host = data['host']
        self.port = int(data['port'])
        self.user = data['user']
        self.pwd = data['pwd']
        self.db = data['db_name']
        self.conn = ''

    def conn_db(self):
        self.conn = pymysql.connect(host=self.host,
                                    port=self.port,
                                    user=self.user,
                                    password=self.pwd,
                                    charset='utf8',
                                    cursorclass=pymysql.cursors.DictCursor,
                                    db=self.db)

    def input_data(self, sql):
        cursor = self.conn.cursor()
        print(cursor.execute(sql))
        self.conn.close()