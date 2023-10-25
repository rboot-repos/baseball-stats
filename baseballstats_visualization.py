import matplotlib.pyplot as plt
import seaborn as sns

# histogram
plt.figure(figsize=(8, 6))
sns.histplot(df['BA'], bins=30, kde=True)
plt.title('Distribution of Batting Averages')
plt.xlabel('Batting Average (BA)')
plt.ylabel('Frequency')
plt.show()

# home runs vs. RBIs
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='HR', y='RBI', alpha=0.7)
plt.title('Home Runs vs. Runs Batted In')
plt.xlabel('Home Runs (HR)')
plt.ylabel('Runs Batted In (RBI)')
plt.show()
