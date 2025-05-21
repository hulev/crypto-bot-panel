
import streamlit as st
import requests

STATUS_URL = "https://api.hulevbot.org/status"

st.set_page_config(page_title="Crypto Bot Control Panel", layout="wide")

st.title("🤖 Crypto Bot Control Panel")

status = {"sniper_bot": False, "rsi_bot": False}
try:
    status = requests.get(STATUS_URL, timeout=5).json()
except Exception as e:
    st.warning("Bot status API unavailable.")

col1, col2 = st.columns(2)
with col1:
    st.subheader("🎯 Sniper Bot")
    if status.get("sniper_bot"):
        st.success("Sniper Bot: Running")
    else:
        st.error("Sniper Bot: Not running")

with col2:
    st.subheader("📈 RSI Bot")
    if status.get("rsi_bot"):
        st.success("RSI Bot: Running")
    else:
        st.error("RSI Bot: Not running")

st.markdown("---")
st.header("Log DB Summary:")
try:
    with open("trade_logs.db", "r") as f:
        st.code(f.read())
except FileNotFoundError:
    st.info("trade_logs.db not found. Logs will appear here once available.")

st.markdown("---")
if st.button("🚨 EMERGENCY STOP ALL"):
    st.warning("Emergency stop issued (placeholder).")
