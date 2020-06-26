import pandas as pd
import numpy as np

class DescriptiveAnalysis:

    def __init__(self, dataframe):
        self.df = dataframe
        self.columns = dataframe.columns
        self.numerical_columns = [var for var in dataframe if dataframe[var].dtypes != 'O']
        self.categorical_columns = [var for var in dataframe if dataframe[var].dtypes == 'O']
        self.binary_columns = [var for var in dataframe if len(dataframe[var].dropna().value_counts()) <= 2]
        self.null_columns = dataframe.columns[dataframe.isnull().any()] 
        #self.missing_values = 

    def overview(self):

        try:
            col = ['Dataset statistics','Count']
            dataset_overview = pd.DataFrame(columns = col)
            dataset_overview.loc[0] = ['Number of observations',self.df.shape[0]]
            dataset_overview.loc[1] = ['Number of variables',self.df.shape[1]]
            dataset_overview.loc[2] = ['Categorical variables',len(self.categorical_columns)]
            dataset_overview.loc[3] = ['Numeric variables',len(self.numerical_columns)]
            dataset_overview.loc[4] = ['Binary variables',len(self.binary_columns)]
            dataset_overview.loc[5] = ['Missing value columns',len(self.df.columns[self.df.isnull().any()])]
            dataset_overview.loc[6] = ['Missing cells',self.df.isnull().sum().sum()]
            dataset_overview.loc[7] = ['Missing cells (%)',np.round(self.df.isnull().sum().sum()/(self.df.shape[0] * self.df.shape[1]),4)*100]      
            return dataset_overview
        except Exception as e:
            return e

    def categorical_variables(self):

        try:
            i = 0
            col = ['Categorical Variables','Distinct Count','Missing Values','Missing Values (%)']
            catg_variables = pd.DataFrame(columns = col)
            for var in self.categorical_columns:    
                catg_variables.loc[i] = [var,
                                        self.df[var].nunique(),
                                        self.df[var].isnull().sum(),
                                        np.round(self.df[var].isnull().sum()/self.df.shape[0],4)*100]
                i+=1
            return catg_variables
        except Exception as e:
            return e

    def quantile_stats(self):

        try:
            i = 0
            col = ['Numerical Variables','Min','5-th perc','Q1','Median','Q3','95-th perc','Max','IQR']
            quantile = pd.DataFrame(columns = col)
            for var in self.numerical_columns:    
                quantile.loc[i] = [var,
                                    np.round(self.df[var].dropna().min(),2),
                                    np.round(np.percentile(self.df[var].dropna(), 5),2),
                                    np.round(np.percentile(self.df[var].dropna(), 25),2),
                                    np.round(np.percentile(self.df[var].dropna(), 50),2),
                                    np.round(np.percentile(self.df[var].dropna(), 75),2),
                                    np.round(np.percentile(self.df[var].dropna(), 95),2),
                                    np.round(self.df[var].dropna().max(),2),
                                    np.round(np.subtract(*np.percentile(self.df[var].dropna(), [75, 25])),2)
                                    ]
                i+=1
            return quantile
        except Exception as e:
            return e
        
    def numerical_variables(self):

        try:
            i = 0
            col = ['Numerical Variables','Distinct Count','Missing Values','Missing Values (%)','Zeros','Mean','Median','Range','SD']
            num_overview = pd.DataFrame(columns = col)
            for var in self.numerical_columns:    
                num_overview.loc[i] = [var,
                                    self.df[var].nunique(),
                                    self.df[var].isnull().sum(),
                                    np.round(self.df[var].isnull().sum()/self.df.shape[0],4)*100,
                                    self.df[var][self.df[var] == 0].count(),
                                    np.round(self.df[var].dropna().mean(),2),
                                    np.round(self.df[var].dropna().median(),2),
                                    np.round(self.df[var].dropna().max() - self.df[var].dropna().min(),2),
                                    np.round(np.std(self.df[var]),2)
                                    ]
                i+=1
            return num_overview
        except Exception as e:
            return e

    def binary_variables(self):
        try:
            return pd.DataFrame({'Dtype' : self.df[self.binary_columns].dtypes}).reset_index()
        except Exception as e:
            return e
            
    def null_variables(self):

        try:
            i = 0
            col = ['Null Variables', 'Dtype', 'Null Occurance', '% Null'] 
            null_variables = pd.DataFrame(columns = col)             

            for var in self.null_columns:
                null_variables.loc[i]  = [var,
                                        self.df[var].dtypes,
                                        self.df[var].isnull().sum(),
                                        np.round( self.df[var].isnull().sum() / self.df[var].shape[0] * 100,2)]
                i+=1
            return null_variables 
        except Exception as e:
            return e

    def unique_values(self,column_target):

        try:
            unique_values = self.df[column_target].value_counts().to_frame().reset_index()
            unique_values.sort_values(by='index', inplace=True)
            unique_values.rename(columns={'index':column_target, '{}'.format(column_target):"Values Frequency"}, inplace=True)
            return unique_values
        except Exception as e:
            return e