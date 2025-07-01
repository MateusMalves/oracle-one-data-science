# # #
# بِسْمِ ٱللّٰهِ ٱلرَّحْمٰنِ ٱلرَّحِيمِ
# Bismillāh ir-raḥmān ir-raḥīm
# 
# In the name of God, the Most Gracious, the Most Merciful
# Em nome de Deus, o Clemente, o Misericordioso
# # #
# # #


# #
# Imports
import pandas as pd
import matplotlib.pyplot as plt

def label_plot(title: str = '', xlabel: str = '', ylabel: str = '', footer: str = '', fontsizes: str = 'medium') -> None:
    """
    Adds a title, axis labels, and optional footer to a Matplotlib plot.

    Parameters
    ----------
    title : str, optional
        Title of the plot.  
        Default is '' (no title).
    xlabel : str, optional
        Label for the x-axis.  
        Default is '' (no label).
    ylabel : str, optional
        Label for the y-axis.  
        Default is '' (no label).
    footer : str, optional
        Footer text to be displayed below the plot.  
        Default is '' (no footer).
    fontsizes : {'small', 'medium', 'large'}, optional
        Font size preset for the plot elements. Determines relative sizes for
        title, axis labels, and footer.  
        Default is 'medium'.

    Returns
    -------
    None
    """
    # Setup fontsizes
    fontsizes = fontsizes.strip().lower()
    if fontsizes not in ['small', 'medium', 'large']:
        fontsizes = 'medium'
    
    font_sizes = {}
    if fontsizes == 'small':
        font_sizes = {
            'title': 'large',
            'labels': 'small',
            'footer': 'medium'
        }
    elif fontsizes == 'medium':
        font_sizes = {
            'title': 'x-large',
            'labels': 'medium',
            'footer': 'large'
        }
    elif fontsizes == 'large':
        font_sizes = {
            'title': 'xx-large',
            'labels': 'large',
            'footer': 'x-large'
        }

    if title:
        plt.title(title, fontsize=font_sizes['title'])
    if xlabel:
        plt.xlabel(xlabel, fontsize=font_sizes['labels'])
    if ylabel:
        plt.ylabel(ylabel, fontsize=font_sizes['labels'])
    if footer:
        plt.text(0.5, -0.025, footer, ha='center', va='top',
                 transform=plt.gcf().transFigure, fontsize=font_sizes['footer'])
        
    # Adjust layout for cases of too much text in the plot
    if title and xlabel and ylabel:
        if footer:
            plt.tight_layout(rect=(0, 0.05, 1, 1))
        else:
            plt.tight_layout()


def plot_central_tendency(
        column: pd.Series,
        axis: int = 0,
        linewidth: int = 1,
        colors: list[str] = ['red', 'yellow', 'blue']
) -> None:
    """
    Plots vertical lines for mean, median, and mode of a numeric column on an existing histogram or plot.

    Parameters
    ----------
    column : pd.Series
        The column to analyze.
    axis : int, optional
        Axis for the lines:  
        0 = vertical (x-axis)  
        1 = horizontal (y-axis).  
        Default is 0.
    linewidth : int, optional
        Width of the plotted vertical lines.  
        Default is 1.
    colors : list[str], optional
        List of 3 colors for mean, median, and mode lines respectively.  
        Default is ['red', 'yellow', 'blue'].

    Raises
    ------
    TypeError or ValueError if inputs are invalid.

    Returns
    -------
    None
    """
    # Validate input parameters
    if not isinstance(column, pd.Series):
        raise TypeError('column must be a pandas Series')
    if not pd.api.types.is_numeric_dtype(column):
        raise TypeError(f"column must be numeric")
    
    # Validate axis, linewidth and colors
    if not isinstance(axis, int) or axis not in [0, 1]:
        axis = 0
    if not isinstance(linewidth, int) or linewidth < 1:
        linewidth = 1
    if isinstance(colors, tuple) and len(colors) == 3 and all(isinstance(c, str) for c in colors): # Tolerates a tuple
        colors = list(colors)
    if not isinstance(colors, list) or len(colors) != 3 or not all(isinstance(c, str) for c in colors):
        colors = ['red', 'yellow', 'blue']


    # Calculate the mean, median, and mode
    mean = column.mean()
    median = column.median()
    mode = column.mode().values[0]
    
    # Create a dictionary for colors
    colors_dict = {
        'mean': colors[0],
        'median': colors[1],
        'mode': colors[2]
    }

    # Plot the lines
    if axis == 0:
        plt.axvline(mean, color=colors_dict['mean'], linestyle='dashed', linewidth=linewidth)
        plt.axvline(median, color=colors_dict['median'], linestyle='dashed', linewidth=linewidth)
        plt.axvline(mode, color=colors_dict['mode'], linestyle='dashed', linewidth=linewidth)
    elif axis == 1:
        plt.axhline(mean, color=colors_dict['mean'], linestyle='dashed', linewidth=linewidth)
        plt.axhline(median, color=colors_dict['median'], linestyle='dashed', linewidth=linewidth)
        plt.axhline(mode, color=colors_dict['mode'], linestyle='dashed', linewidth=linewidth)
    
    plt.legend([f'Mean: {mean:.2f}', f'Median: {median:.2f}', f'Mode: {mode:.2f}'])