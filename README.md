# Streamlit [MotherDuck](https://motherduck.com) Connection 🦆

Connect to [MotherDuck](https://motherduck.com) from your Streamlit app seamlessly. This library, powered by `st.experimental_connection()`, offers a straightforward interface to establish and manage your connection to a [MotherDuck](https://motherduck.com) database.

## 🌟 Features
- Simple connection establishment to [MotherDuck](https://motherduck.com) using DuckDB.
- Execute SQL queries and fetch results as DataFrames.
- Cache support for repetitive queries to boost performance.

## 🔧 Installation
\```bash
pip install motherduck-connection
\```

## 🚀 Usage

### Establishing a Connection
Initiate an instance of the `MotherDuckConnection` class from the `motherduck_connection` module. Optionally provide a database path. If omitted, it'll connect to the default database (`my_db`).

### Executing Queries
Use the `query` method of the `MotherDuckConnection` instance to run SQL queries and fetch results.

## 📖 Example Application: `app.py`

This example showcases how you can employ the `MotherDuckConnection` library in a Streamlit app to query [MotherDuck](https://motherduck.com).

### 🌐 Features:
1. **DuckDB Table Query**: Showcases a table from [MotherDuck](https://motherduck.com)'s sample data, displaying the top 20 stories from Hacker News. 
2. **Replies to a HN Post**: Lets users input a Hacker News post ID and fetches related replies.
3. **Current HN Front Page**: Displays the present front page of Hacker News.

### 🏃 Running the Example:
Navigate to the `examples` directory and run:
\```bash
streamlit run app.py
\```

## 📚 Helper Functions: `motherduck_sql.py`

Offers functions to aid in querying data from [MotherDuck](https://motherduck.com) and the Hacker News API.

### 📋 Functions:
1. **get_hn_item(id)**: Fetches the URL to retrieve an item from Hacker News.
2. **get_hn_front_page()**: Gets the URL for Hacker News front page items.
3. **query_hn_front_page(conn)**: Queries Hacker News front page with a [MotherDuck](https://motherduck.com) connection, returning a DataFrame.
4. **query_hn_items(conn, hn_item_id_input)**: Fetches an item and its comments from Hacker News based on a given ID.
5. **query_motherduck(conn, table_name)**: Queries a table from [MotherDuck](https://motherduck.com), fetching 'story' type items.

## 📜 License
See the [LICENSE](LICENSE) file for details.