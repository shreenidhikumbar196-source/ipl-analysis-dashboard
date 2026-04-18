import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="IPL Analysis Dashboard", page_icon="🏏", layout="wide")

st.title("🏏 IPL Complete Analysis Dashboard")
st.markdown("---")

# Load data
matches = pd.read_csv('matches.csv')
deliveries = pd.read_csv('deliveries.csv')

# Sidebar
st.sidebar.title("🏏 IPL Dashboard")
option = st.sidebar.selectbox("Choose Analysis", [
    "Team Performance",
    "Top Batsmen",
    "Top Bowlers",
    "Player of Match",
    "Toss Impact"
])

if option == "Team Performance":
    st.header("🏆 Top 10 Winning Teams")
    top_teams = matches['winner'].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=top_teams.values, y=top_teams.index, palette='Oranges_r', ax=ax)
    ax.set_xlabel("Number of Wins")
    ax.set_title("Top 10 IPL Winning Teams")
    st.pyplot(fig)

elif option == "Top Batsmen":
    st.header("🏏 Top 10 Run Scorers")
    top_batsmen = deliveries.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=top_batsmen.values, y=top_batsmen.index, palette='Blues_r', ax=ax)
    ax.set_xlabel("Total Runs")
    ax.set_title("Top 10 IPL Run Scorers")
    st.pyplot(fig)

elif option == "Top Bowlers":
    st.header("🎳 Top 10 Wicket Takers")
    wickets = deliveries[deliveries['dismissal_kind'].notna()]
    top_bowlers = wickets.groupby('bowler')['dismissal_kind'].count().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=top_bowlers.values, y=top_bowlers.index, palette='Greens_r', ax=ax)
    ax.set_xlabel("Total Wickets")
    ax.set_title("Top 10 IPL Wicket Takers")
    st.pyplot(fig)

elif option == "Player of Match":
    st.header("🌟 Top 10 Player of the Match")
    top_players = matches['player_of_match'].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=top_players.values, y=top_players.index, palette='Purples_r', ax=ax)
    ax.set_xlabel("Number of Awards")
    ax.set_title("Top 10 Player of the Match Winners")
    st.pyplot(fig)

elif option == "Toss Impact":
    st.header("🪙 Does Toss Impact Match Result?")
    matches['toss_match_winner'] = matches['toss_winner'] == matches['winner']
    toss_impact = matches['toss_match_winner'].value_counts()
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(toss_impact.values, labels=['Won Toss & Match', 'Won Toss Lost Match'],
           autopct='%1.1f%%', colors=['#ff9999','#66b3ff'])
    ax.set_title("Toss Impact on Match Result")
    st.pyplot(fig)

st.markdown("---")
st.markdown("Built by **Shreenidhi** | Data Source: Kaggle IPL Dataset")