import seaborn as sns
import matplotlib.pyplot as plt


def visualize_bivariate(plot_type,df,x_axis, y_axis):
    """
    plot bivariate graph 
    Args:
        plot_type: Type of plot to draw
        df: data frame
        x_axis: the first variable on the x axis
        y_axis: the sceond variable on the y axis
    """
    if(plot_type == 'lineplot'):
        sns.lineplot(df, x=x_axis, y=y_axis, palette = 'Set2')
    elif(plot_type == 'scatterplot'):
        sns.scatterplot(df, x='date', y='count', color='blue')
    else:
        sns.barplot(df, x='date', y='count', color='blue')

    plt.figure(figsize=(12, 6))
    plt.title( x_axis + "vs." + y_axis)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.show()


