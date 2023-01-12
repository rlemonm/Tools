import pymysql
import logging

_LOGGER = logging.getLogger(__name__)


class DbUtils():
    def __init__(self, host: str, port: int, user: str, password: str, database: None, charset='utf-8') -> None:
        """
        :param host:
        :param port:
        :param user:
        :param password:
        :param database:
        :param charset:
        """
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset

    def conn(self):
        """
        connect db
        :return: cursor
        """
        try:
            conn = pymysql.connect(host=self.host,
                                   port=self.port,
                                   user=self.user,
                                   password=self.password,
                                   database=self.database)
            cur = conn.cursor()
            _LOGGER.info("connect db %s and create cursor success", self.database)
            return cur
        except Exception as e:
            _LOGGER.error(e)

    @classmethod
    def close_conn(cls):
        # TODO
        pass

    def fetch_one_data(self):
        # TODO
        pass

    def fetch_all_data(self):
        # TODO
        pass

    def operate_db(self):
        # TODO
        pass

    def insert_data(self):
        # TODO
        pass

    def del_data(self):
        # TODO
        pass

    def update_data(self):
        # TODO
        pass
