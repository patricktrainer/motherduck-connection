# Streamlit MotherDuck connection

Connect to MotherDuck from your Streamlit app. Powered by `st.experimental_connection()`

## Running the example

Run the example with:

```bash
streamlit run examples/app.py
```

This will start a Streamlit app that connects to MotherDuck. 

MotherDuck will prompt you to authorize the connection. Once you do, you'll see the app print out the data it receives from MotherDuck. 

You can export the connection token so that you don't have to authorize the connection every time you run the app:
```bash
export motherduck_token=<your token>
```

![image](https://github.com/patricktrainer/motherduck-connection/assets/36834097/4ab6b086-6436-4f92-8145-e80912fbd92f)
