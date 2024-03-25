import matplotlib.pyplot as plt
import seaborn as sns

def plot_pairplot(df):
    sns.pairplot(df, hue='target_names')
    plt.show()

def plot_heatmap(df):
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.show()
