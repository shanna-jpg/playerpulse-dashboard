import streamlit as st
import pandas as pd
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect(r"C:\Users\shanna\Documents\PlayerPulse\playerpulse.db")

# Load tables
teams_df = pd.read_sql_query("SELECT * FROM teams;", conn)
players_df = pd.read_sql_query("SELECT * FROM players;", conn)
games_df = pd.read_sql_query("SELECT * FROM games;", conn)
player_stats_df = pd.read_sql_query("SELECT * FROM player_game_stats;", conn)

conn.close()

st.title("PlayerPulse Dashboard")

# --- Teams Table ---
st.subheader("Teams")
st.dataframe(teams_df)

# --- Players Table ---
st.subheader("Players")
st.dataframe(players_df)

# --- Games Table (without score column) ---
st.subheader("Games")
if 'score' in games_df.columns:
    games_df_no_score = games_df.drop(columns=['score'])
else:
    games_df_no_score = games_df.copy()
st.dataframe(games_df_no_score)

# --- Player Game Stats Table ---
st.subheader("Player Game Stats")
st.dataframe(player_stats_df)