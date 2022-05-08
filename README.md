# Wine Quality

## Project Overview

#### Selected topic: Wine Quality Prediction

Here we will predict the quality of wine on the basis of giving features. We are using the wine quality dataset from Kaggle. This dataset has the fundamental features which are responsible for affecting the quality of the wine. By the use of several Machine learning models, we will predict the quality of the wine.

#### Technologies used

- Python
- Jupyter Notebooks
- Numpy
- Pandas 
- Matplotlib
- Tableau 
- scikit-learn 
- 

#### Reason why we selected this topic: 

We had a similar interest in wine and were curious on which characteritics of wine affects its quality. We also want to predit what kind of wines could possibly win certain wine competitions.  

#### Description of the source of data: 

We found a dataset to start with that have multiple features for diffrent kinds of wines, such as pH and density. 
  - https://www.kaggle.com/rajyellow46/wine-quality

Dataset description: These are the name of Features from the dataset

_Input Variables_

- Fixed acidity : The predominant fixed acids in wine, such as tartaric, succinic, citric, and malic acids.
- Volatile acidity : The high acetic acid present in wine, which causes an unpleasant vinegar taste.
- Citric acid : A weak organic acid used to increase the freshness and flavor of wine.
- Residual sugar : The amount of sugar left after fermentation.
- Chlorides : The amount of salt in wine. The lower chloride rate creates better quality wines.
- Free sulfur dioxide : SO2 is used for preventing wine from oxidation and microbial spoilage.
- Total sulfur dioxide : The amount of free and bound forms of SO2.
- Density : Depends on the alcohol and sugar content. Better wines usually have lower densities.
- pH : Used to check the level of acidity or alkalinity of wine.
- Sulphates : An antibacterial and antioxidant agent added to wine.
- Alcohol : The percentage of alcohol in wine. A higher concentration leads to better quality.

_Output Variable_

- Quality score : The quality rating of wine that is based on sensory data and scores from 0 to 10. 

#### Questions that we hope to answer with the data: 

We hope to find out what makes certain wines have a higher quality than others. 

####  Description of the communication protocols

The group keep discussing the project details during live sessions and constantly making contact with each other through the slack app, including sharing of information and data that we find online.

## Machine Learning FlowChart

### DataSet
Wine Quality DataSet

### What type of input data?
* Label:
* Classification:
* Large number of variables:
* Non-tabular:

### What type of data cleaning?
* Remove any values that have null or undefined values. If there are any values missing in a particular column, we might drop it. If we see that a particular wine has a high/low quality with a missing value, such as pH. We can possibly predict the pH by comparing to other records with similar chemical make-up and do additional research in order to potentially add a new accurate value for the missing cell.
* Remove any columns that don't affect the wine quality. For example, residual sugars and chlorides don't seem to effect the quality of wine, considering they have a low correlation between both variables, we would drop these two columns.
* Sometimes, the wine names have special characters, which might not be able to pass through Jupyter Notebook, and when downloaded or uploaded as a CSV, so information might be lost. To avoid this, I plan to change some fo the special names so thatthey can pass through Jupyter Notebook without any errors. I will also add a unique ID number so that we can easily match the wines at the end.

### Feature Engineering Required?
 ### Additions to the DataSet
* Wine types (White, Red) 
* Styles (Sparkling, Light-bodied White, Full-Bodied White, Light-Bodied Red, Full-Bodied Red, Dessert, Rosé, etc.)
* List Price

### What is the Machine Learning Model?
* Supervised Machine Learning

### How are you evaluating and testing the Machine Learning model?
* Linear Regression Model
