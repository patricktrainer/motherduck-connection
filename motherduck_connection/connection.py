from pandas import DataFrame
from streamlit.connections import ExperimentalBaseConnection
from streamlit.runtime.caching import cache_resource

import duckdb


class MotherDuckConnection(
    ExperimentalBaseConnection[duckdb.DuckDBPyConnection]
):
    def _connect(self, database=None, **kwargs) -> duckdb.DuckDBPyConnection:
        """
        Creates a connection to MotherDuck.

        Args:
            database (str): The path to the DuckDB database.
            If no path is given, the connection will use the
            default database set in MotherDuck (my_db).

        Returns:
            A DuckDBPyConnection object representing the connection to the database.
        """

        url_scheme: str = "motherduck:"
        if database is None:
            database = "my_db"
        
        return duckdb.connect(f"{url_scheme}{database}", **kwargs)

    def query(self, query: str) -> duckdb.DuckDBPyRelation:
        """
        Executes a SQL query and returns the result as a DataFrame.

        Args:
            query (str): The SQL query to execute.

        Returns:
            DataFrame: The result of the query as a DataFrame.
        """

        @cache_resource
        def _query(_self, query: str):
            conn = _self._connect()

            return conn.sql(query=query)

        return _query(self, query)
