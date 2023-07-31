import unittest
import duckdb
from pandas import DataFrame

from motherduck_connection.connection import MotherDuckConnection


class TestMotherDuckConnection(unittest.TestCase):
    def setUp(self):
        self.connection = MotherDuckConnection("motherduck")

    def test_query(self):
        query = "SELECT current_schema();"
        result = self.connection.query(query)
        self.assertIsInstance(result, DataFrame)

    def test_connect(self):
        connection = self.connection._connect()
        self.assertIsInstance(connection, duckdb.DuckDBPyConnection)

if __name__ == '__main__':
    unittest.main()