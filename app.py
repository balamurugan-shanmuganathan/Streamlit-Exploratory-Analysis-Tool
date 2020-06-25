import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from DescriptiveAnalysis.DescriptiveAnalysis import DescriptiveAnalysis
from ExploratoryAnalysis.ExploratoryAnalysis import ExploratoryAnalysis

def main():

    st.title('Exploratory Analysis Tool')

    st.info('''Welcome to the Exploratory Analysis Tool. This is a simple application to getting basic information and quick data visualization for generic csv files. Keep in mind that it is not a complete tool and very large files will reduce application performance. If you find a bug or want to help improve this application, the source code is on the link on the left side.''')


    def GetFile():
        uploaded_file = st.file_uploader("", type="csv")
        if uploaded_file is not None:
            return(pd.read_csv(uploaded_file))  

    df = GetFile()   
       
            
    # Basic EDA 
    st.sidebar.subheader('Basic Exploratory Analysis Options')
    st.sidebar.title('Menu')
    if st.sidebar.checkbox('Basic Informations'):  
        st.title('Dataframe Basic Info')   
        DA = DescriptiveAnalysis(df)       
        # Head
        if st.sidebar.checkbox('Head'):
            st.subheader('Dataframe Head:')
            st.write(df.head(10))
        # Info
        if st.sidebar.checkbox('Informations'):
            st.subheader('Dataframe Informations:')
            st.write(DA.overview())

        # About Categorical Variables
        if st.sidebar.checkbox('Categorical Variables'):
            st.subheader('Categorical Variables Informations:')
            st.write(DA.categorical_variables())
        
        # About Numerical Variables
        if st.sidebar.checkbox('Numerical Variables'):
            st.subheader('Numerical Variables Informations:')
            st.write(DA.numerical_variables())

            if st.checkbox('Quantile Statistics'):
                st.write(DA.quantile_stats())

        if st.sidebar.checkbox('Binary Variables'):
            st.subheader('Binary Variables Informations:')
            st.write(DA.binary_variables())

        if st.sidebar.checkbox('Null Variables'):
            st.subheader('Null occurrences')
            st.write(DA.null_variables())
        
        if st.sidebar.checkbox('Unique values and frequency'):
            column_target = st.sidebar.selectbox('Choose a column for see unique values',DA.columns)
            st.subheader('Unique values and frequency')
            st.write(DA.unique_values(column_target))
    
    
    st.sidebar.subheader('Data visualization options')

    if st.sidebar.checkbox('Graphics'):
        st.title('Dataframe plots')
        EA = ExploratoryAnalysis(df)
        if st.sidebar.checkbox('Count Plot'):
            st.subheader('Count Plot')
            column_count_plot = st.sidebar.selectbox("Choose a column to plot count",EA.columns)
            hue_opt = st.sidebar.selectbox("Optional categorical variables (countplot hue)",EA.columns.insert(0,None))
            if st.checkbox('Plot Countplot'):
                fig = EA.CountPlot(column_count_plot, hue_opt)
                st.pyplot()

        if st.sidebar.checkbox('Distribution Plot'):
            st.subheader('Distribution Plot')
            column_dist_plot = st.sidebar.selectbox("Choose a column to plot distribution (only numerical)",EA.numerical_columns)
            if st.checkbox('Plot Distplot'):
                fig = EA.DistPlot(column_dist_plot)
                st.pyplot()
            
        if st.sidebar.checkbox('Heatmap Correlation'):
            st.subheader('Heatmap Correlation Plot')
            annot = None
            if st.checkbox('Annot'):
                annot = True
            fig = EA.HeatMapCorr(annot = annot)
            st.pyplot()

        if st.sidebar.checkbox('Boxplot'):
            st.subheader('Boxplot')
            column_box_plot_X = st.sidebar.selectbox("X (Choose a column):",EA.columns.insert(0,None))
            column_box_plot_Y = st.sidebar.selectbox("Y (Choose a column - only numerical):",EA.numerical_columns)
            hue_box_opt = st.sidebar.selectbox("Optional categorical variables (boxplot hue)",EA.columns.insert(0,None))
            if st.checkbox('Plot Boxplot'):
                fig = EA.BoxPlot(column_box_plot_X, column_box_plot_Y, hue_box_opt)
                st.pyplot()

        if st.sidebar.checkbox('Pairplot'):
            st.subheader('Pairplot')
            hue_pp_opt = st.sidebar.selectbox("Optional categorical variables (pairplot hue)",EA.columns.insert(0,None))
            st.info("This action may take a while.")
            if st.checkbox('Plot Pairplot'):
                fig = EA.PairPlot(hue_pp_opt)
                st.pyplot()



    #st.sidebar.markdown("**Help me to improve this application. See the source code below. Follow me!**")
    st.sidebar.markdown("**Github Profile:**")
    st.sidebar.markdown("[Balamurugan S](https://github.com/balamurugan-shanmuganathan)")
    st.sidebar.markdown(" ` Version 0.0.1 ` ")
    
if __name__ == '__main__':
    main()