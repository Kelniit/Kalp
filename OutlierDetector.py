import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set_style('whitegrid')

class OutlierDetectorClass:
  def __init__(self, table):
    """
    Outlier Detector Class

    >>> outlier = OutlierDetectorClass(table)
    """
    self.table = table

  def InterQuartile(self, column):
    """
    Inter Quartile Outlier Range

    >>> outlier.InterQuartile('mean_ip')
    """
    UnderQuartile = np.percentile(self.table[column], 25)
    UpperQuartile = np.percentile(self.table[column], 75)
    InterQuartileResult = UpperQuartile - UnderQuartile
    LowerBound = UnderQuartile - 1.5 * InterQuartileResult
    UpperBound = UpperQuartile + 1.5 * InterQuartileResult
    Result = [i for i, x in enumerate(self.table[column]) if x < LowerBound or x > UpperBound]
    return Result

  def OutlierPlot(self, column, label, title):
    """
    Box Plot to Check Outlier

    >>> label = 'Mean of Integrated Profile'
    >>> title = str(label) + ' Outlier'
    >>> outlier.OutlierPlot('mean_ip', label, title)
    """
    ploti = sns.boxplot(self.table[column])
    ploti.set_title(title)
    ploti.set_ylabel(label)
    plt.show()