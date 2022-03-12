import mariadb
import argparse
import configparser


def arg_reader():
    parser = argparse.ArgumentParser()
    parser.add_argument('--conf', type=str, default='db_conf.txt')
    return parser.parse_args().conf


def conf_reader(conf_file):
    result = dict()
    conf = configparser.ConfigParser()
    conf.read(conf_file)
    for i in conf.sections():
        for j in conf.options(i):
            result[j] = conf[i][j]
    return result


def main():
    sql = 'SHOW TABLES'
    db = mariadb.MariaDB(conf_reader(arg_reader()))
    db.conn_db()
    db.input_data(sql)


if __name__ == '__main__':
    main()
    # print(conf_reader(arg_reader()))
    # pass
