import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def CalculateMeanAbsoluteDeviation(deviation):
    return np.absolute(deviation).mean()

def DrawLineChartFromDataFrame(df):
    fig = plt.figure()
    plt.style.use('ggplot')
    df.plot()
    plt.xticks(rotation=90)
    plt.show()
    return fig
