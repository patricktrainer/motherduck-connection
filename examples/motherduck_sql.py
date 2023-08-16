def get_hn_item(id):
    return f"http://hn.algolia.com/api/v1/items/{id}"


def get_hn_front_page():
    hn_api_front_page = "http://hn.algolia.com/api/v1/search?tags=front_page"
    return hn_api_front_page


def query_hn_front_page(conn) -> None:
    hn_api_front_page = get_hn_front_page()
    front_page_response = conn._instance.sql(
        query=f"""
        with hits as (
                select 
                    row(j.hits) as hits
                from read_json_auto('{hn_api_front_page}') as j 
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
    return front_page_response


def query_hn_items(conn, hn_item_id_input) -> None:
    # only run the query if the user has entered a valid value
    if not hn_item_id_input:
        pass  # do nothing
    else:
        hn_api_item = get_hn_item(hn_item_id_input)
        hn_items_response = conn._instance.sql(
            f"""
        with q as (
                select 
                    unnest(row(j.id, j.children)) as c,
                from read_json_auto('{hn_api_item}') as j
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
        return hn_items_response


def query_motherduck(conn, table_name):
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
        from {table_name}
        where type = 'story'
        order by score desc
        limit 20
        """
    ).df()
    return hn_sample_response
