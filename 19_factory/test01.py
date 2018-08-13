#!/usr/bin/python3

from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connection(self):
        pass

    

class SqlServer:
    def connection(self):
        return 'Sql datebase connection'


class Oracle:
    def connection(self):
        return 'Oracle database connection'


class DbFactory:
    def __init__(self, database):
        self.database = database

    def connection(self):
        return self.database.connection()


if __name__=="__main__":
    factory1 = DbFactory(SqlServer())
    factory2 = DbFactory(Oracle())

    print(factory1.connection())
    print(factory2.connection())
