import seaborn as sns
import matplotlib.pyplot as plt

def visualize_bivariate(df,x_axis, y_axis):
    sns.lineplot(data=df, x=x_axis, y=y_axis, palette = 'Set2')
    plt.title("Impact of" & x_axis & "vs." & y_axis)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.show()