import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
matches = pd.read_csv('matches.csv')
deliveries = pd.read_csv('deliveries.csv')

# ---- ANALYSIS 1: Most successful teams ----
print("=== TOP 10 WINNING TEAMS ===")
top_teams = matches['winner'].value_counts().head(10)
print(top_teams)

# ---- ANALYSIS 2: Toss impact ----
matches['toss_match_winner'] = matches['toss_winner'] == matches['winner']
toss_impact = matches['toss_match_winner'].value_counts()
print("\n=== TOSS IMPACT ===")
print(toss_impact)

# ---- ANALYSIS 3: Top Player of Match ----
print("\n=== TOP 10 PLAYER OF THE MATCH ===")
print(matches['player_of_match'].value_counts().head(10))

# ---- ANALYSIS 4: Top run scorers ----
print("\n=== TOP 10 RUN SCORERS ===")
top_batsmen = deliveries.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10)
print(top_batsmen)

# ---- ANALYSIS 5: Top wicket takers ----
print("\n=== TOP 10 WICKET TAKERS ===")
wickets = deliveries[deliveries['dismissal_kind'].notna()]
top_bowlers = wickets.groupby('bowler')['dismissal_kind'].count().sort_values(ascending=False).head(10)
print(top_bowlers)

print("\n✅ Analysis complete!")