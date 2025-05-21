import streamlit as st
import pandas as pd
import sqlite3
from pathlib import Path

st.set_page_config(page_title="Bot Control Panel", layout="wide")

st.title("🤖 Crypto Bot Control Panel")

status_cols = st.columns(2)
status_cols[0].error("Sniper Bot: Not running")
status_cols[1].error("RSI Bot: Not running")

st.write("---")

st.subheader("Log DB Summary:")
db_path = Path("trade_logs.db")
if db_path.exists():
    conn = sqlite3.connect(db_path)
    df = pd.read_sql("SELECT * FROM trades ORDER BY timestamp DESC LIMIT 50", conn)
    conn.close()
    st.dataframe(df)
else:
    st.info("trade_logs.db not found. Logs will appear here once available.")

st.write("---")
st.button("🚨 EMERGENCY STOP ALL", disabled=True)
