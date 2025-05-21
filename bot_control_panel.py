
import streamlit as st
import subprocess
import json
import os
from datetime import datetime

# === CONFIG ===
SNIPER_CMD = "python aggressive_sniper_bot.py"
RSI_CMD = "python rsi_trade_bot.py"
import requests

STATUS_URL = "https://0e909cb3ac8968.lhr.life/status"

def load_bot_status():
    try:
        response = requests.get(STATUS_URL)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print("Error loading status:", e)
    return {"rsi_bot": False, "sniper_bot": False}

# For process tracking
running_processes = {}

# === UTILS ===
def get_last_action(file, limit=3):
    if not os.path.exists(file):
        return []
    with open(file, "r") as f:
        lines = f.readlines()[-limit:]
    return [line.strip() for line in lines]

def load_state(file):
    if not os.path.exists(file):
        return {}
    with open(file, "r") as f:
        return json.load(f)

# === DASHBOARD UI ===
st.set_page_config(page_title="Bot Control Panel", layout="centered")
st.title("🤖 Crypto Bot Control Panel")

status = load_bot_status()

col1, col2 = st.columns(2)

with col1:
    st.subheader("🎯 Sniper Bot")
    if status["sniper_bot"]:
        st.success("Sniper Bot: Running")
    else:
        st.error("Sniper Bot: Not running")

with col2:
    st.subheader("📈 RSI Bot")
    if status["rsi_bot"]:
        st.success("RSI Bot: Running")
    else:
        st.error("RSI Bot: Not running")
