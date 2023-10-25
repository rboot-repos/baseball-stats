df = pd.read_csv('mlb_batting_stats_2022.csv')

summary_stats = df.describe()

# (BA)
average_ba = df['BA'].mean()

# (HR) count
top_homerun_hitters = df.nlargest(10, 'HR')

# home runs and RBIs
correlation = df['HR'].corr(df['RBI'])
