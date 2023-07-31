from motherduck_connection import MotherDuckConnection
import streamlit as st

with st.echo():
    conn = st.experimental_connection("motherduck", type=MotherDuckConnection)

QUERY = """
SELECT
date, project, count(*) as downloads
FROM 'https://motherduck-demo.s3.amazonaws.com/pypi_downloads.parquet'
GROUP BY date, project
ORDER BY date desc;

"""


def get_data(sql, conn):
    return conn.query(query=sql)


data = get_data(QUERY, conn)
st.bar_chart(data, y="downloads", x="date")
st.table(data)
