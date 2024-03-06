
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming you have the necessary data for the plot
data = {
    'country': ['Country A', 'Country B', 'Country C', 'Country D', 'Country E'],
    'total_litres_of_pure_alcohol': [10, 8, 6, 4, 2],
    'spirit_servings': [200, 180, 150, 120, 90]
}

spirit_top = data['spirit_servings']
colors = ['grey' if (s < max(spirit_top)) else 'red' for s in spirit_top]

fig, ax = plt.subplots(figsize=(10, 5))
sns.set_style('white')

ax = sns.barplot(x='country', y='total_litres_of_pure_alcohol',
                 data=data, palette=colors)

plt.title('TOP5 countries by pure alcohol consumption', fontsize=25)
plt.xlabel(None)
plt.xticks(fontsize=16)
plt.ylabel('Litres per person', fontsize=20)
plt.yticks(fontsize=15)

ax.text(x=2.5, y=12.3, s='the highest \nspirit servings',
        color='red', size=17, weight='bold')

sns.despine(bottom=True)
ax.grid(False)
ax.tick_params(bottom=False, left=True)

plt.show()

