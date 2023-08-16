from motherduck_connection import MotherDuckConnection
import streamlit as st
import examples.motherduck_sql as motherduck_sql


st.markdown("## Use MotherDuck to query duckdb, rest apis, and more")
st.markdown("### A duckdb table on MotherDuck")
st.markdown(
    """
    The table below is from the sample data in MotherDuck. 
    From here, a query is run to get the top 20 stories from Hacker News. 
    What's awesome about this is the table is already materialized and ready in MotherDuck.
    This means the query is fast and the data is as fresh as your last sync.
    """
)
conn = st.experimental_connection("motherduck", type=MotherDuckConnection)
st.write(motherduck_sql.query_motherduck(conn, "sample_data.hn.hacker_news"))

st.markdown("### Replies to a post on HN")
input_hn_id = st.text_input(
    label="HN post id",
    placeholder="the number after `item?id=`",
    value="37146532",  # an article about cloud data warehouses
)
st.write(motherduck_sql.query_hn_items(conn, input_hn_id))

st.markdown("### Current front page on HN")
st.write(motherduck_sql.query_hn_front_page(conn))
