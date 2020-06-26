# Exploratory-Analysis-Tool

## Table of Content
 * Demo
 * Overview
 * Motivation
 * Technical Aspects
 * Libraries Used
 * Installation
 * Run
 * Deployement on Heroku
 * Directory Tree
 
### Demo
**Link** : [https://eda-tool-bala.herokuapp.com/](https://eda-tool-bala.herokuapp.com/)

### Overview
This is a simple application to getting basic information and quick data visualization for generic csv file. It is not complete tool and Very large files will reduce application performance.

### Motivation
Whenever we used to practice model with small dataset we keep on doing data visualization from the scratch. It would be waste of time for us to spend on more data visualizaion. To avoid those things I decided to create app for basic EDA.

### Technical Aspects
The project is divided into two parts.
  1. Understanding basic informations about data like shape, info, categorical and numerical features, missing values, frequency table, quantile statistics etc.
  2. Graphical representation of data with bar chart, histogram, box plot, correlation matrix ,pair plot.
 
### Libraries Used
  * Pandas
  * Numpy
  * matplotlib
  * Seaborn
  * Streamlit
  
### Installation
The Code is written in Python 3.7. To install the required packages and libraries, run this command in the project directory after cloning the repository:

 pip install -r requirements.txt

### Run
streamlit run app.py

### Deployement on Heroku
To run app in heroku below mentioned files should be in our repo
   [Procfile](https://github.com/balamurugan-shanmuganathan/Exploratory-Analysis-Tool/blob/master/Procfile)
   [Setup.sh](https://github.com/balamurugan-shanmuganathan/Exploratory-Analysis-Tool/blob/master/setup.sh)

### Directory Tree
    ├── DescriptiveAnalysis 
    │   ├── DescriptiveAnalysis.py
    ├── ExploratoryAnalysis
    │   ├── ExploratoryAnalysis.py
    ├── app.py
    ├── Procfile
    ├── requirements.txt
    ├── Procfile
    ├── README.md
    └── setup.sh
  

