import requests
from motherduck_connection import MotherDuckConnection
import streamlit as st


conn = st.experimental_connection("motherduck", type=MotherDuckConnection)

st.markdown("# Query apis with sql using MotherDuck")
st.markdown("## HN front page")
hn_front_page_endpoint = "http://hn.algolia.com/api/v1/search?tags=front_page"

with st.echo():
    front_page_response = conn._instance.sql(
        f"""
        with hits as (
                select 
                    row(j.hits) as hits
                from read_json_auto('{hn_front_page_endpoint}') as j 
            ),

            h as (
                select
                    unnest(hits, recursive := True) as hit
                from hits
            ),

            final as (
                select
                    unnest(h.hits, recursive := True) as col
                from h
            )

        select 
            objectID::varchar as hn_id,
            created_at,
            author,
            title,
            url,
            points::int as points,
            num_comments
        from final
    """
    ).df()
    st.write(front_page_response)

# st.text_input('hn id', value='37063238')
# pass the id to the query
def get_hn_item_endpoint(id):
    return f"http://hn.algolia.com/api/v1/items/{id}"


hn_item_id_input = st.text_input(label="enter hn id", placeholder='enter a valid hn_id')
hn_items_endpoint = get_hn_item_endpoint(hn_item_id_input)

with st.echo():
    # only run the query if the user has entered a valid value
    if not hn_item_id_input:
        pass # do nothing

    else:
        hn_items_response = conn._instance.sql(
            f"""
            with q as (
                    select 
                        unnest(row(j.id, j.children)) as c,
                    from read_json_auto('{hn_items_endpoint}') as j
                ),

                c as (
                    select 
                        unnest(children) as col 
                    from q
                ),

                final as (
                    select 
                        col.id::varchar as hn_id,
                        col.created_at,
                        col.author,
                        col.text  
                    from c
            )

            select * from final
            """
            ).df()

        st.write(hn_items_response)

st.markdown("# MotherDuck sample data")
mother_duck_fqn = 'sample_data.hn.hacker_news'
with st.echo():
    hn_sample_response = conn._instance.sql(
        f"""
        select 
            id::varchar as hn_id,
            timestamp,
            by as author, 
            title,
            text,
            descendants, -- total count of comments (including nested comments)
            score::int as score,
            url
        from {mother_duck_fqn} 
        where type = 'story'
        order by score desc
        limit 20
        """
    ).df()
    st.write(hn_sample_response)


# st.markdown("## sample_data.hn.hacker_news")
# hn_sample_data = conn._instance.sql(
#     """
#         select 
#             id::varchar as hn_id,
#             timestamp,
#             by as author, 
#             title,
#             text,
#             descendants, -- descendants is the number of top-level comments
#             score::int as score,
#             url
#         from sample_data.hn.hacker_news 
#         where type = 'story'
#         order by score, descendants desc
#         limit 20
#         """
# ).df()
# st.write(hn_sample_data)
