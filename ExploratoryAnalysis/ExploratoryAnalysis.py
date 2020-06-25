import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


# Exploratory Analysis Class
class ExploratoryAnalysis:

    def __init__(self, dataframe):
        self.df = dataframe
        self.columns = dataframe.columns
        self.numerical_columns = [name for name in self.columns if (self.df[name].dtype == 'int64') | (self.df[name].dtype == 'float64')]
    
    def CountPlot(self, column_target, hue=None):
        sns.set(style="darkgrid")
        return sns.countplot(x=column_target, data=self.df, hue=hue, palette='pastel')

    def HeatMapCorr(self, annot =  None):
        sns.set(style="darkgrid")
        sns.set(font_scale=0.6)
        corr = self.df.corr()
        mask = np.zeros_like(corr)
        mask[np.triu_indices_from(mask)] = True
        return sns.heatmap(corr, annot = annot, fmt = '.2f', mask = mask, linewidths = 2, cmap="YlGnBu", vmax = 0.5 )
   
    def DistPlot(self, column_target):
        sns.set(style="darkgrid")
        return sns.distplot(self.df[column_target], color='c')

    def PairPlot(self, hue=None):
        sns.set(style="darkgrid")
        return sns.pairplot(self.df, hue=hue,palette="coolwarm")

    def BoxPlot(self, column_x=None, column_y=None, hue=None):
        sns.set(style="darkgrid")
        return sns.boxplot(x=column_x,y=column_y,hue=hue,data=self.df, palette="Set3")


