from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

# importing the WorldCupMatches.csv
df = pd.read_csv('WorldCupMatches.csv')
#inspecting
#print(df.head())

#print(df.columns)
# Year, Datetime, Stage, Stadium, Home Team Name, Home Team Goals, Away Team Goals, Away Team Name, Win conditions, Attendence, Half-time Home Goals, Half-time Away Goals, Referee, Assistant 1, Assistant 2, RoundID, MatchID, Home Team Initials, Away Team Initials

#print(df.dtypes)
#int, object, object, object, object, int, int, object, object, float, int, int, object, object, object, int, int, object, object

#print(df.info())
#print(df.describe())

#creating a new column where total goals = home team goals + away team goals
df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']
#print(df.head()) 

# making a bar chart years bs total goals

sns.set_style('whitegrid')
sns.set_context('poster', font_scale = 0.75)
f, ax = plt.subplots(figsize=(12, 7))
ax = sns.barplot(data = df, x = 'Year', y = 'Total Goals')
ax.set_title('Total Goals Scored Per Year')
plt.show()
plt.close('all')
plt.clf()

# loading the goals.csv
df_goals = pd.read_csv('goals.csv')
print(df_goals.head())

# changing the plot context to notebook and fontscale to 1.25
f, ax2 = plt.subplots(figsize=(12, 7))
sns.set_context('notebook', font_scale = 1.25)

ax2 = sns.boxplot(data = df_goals, x = 'year', y = 'goals')
ax2.set_title('Distrbution of Goal Scored per Year')
ax2.set_xticks(rotation=30)
plt.show()
