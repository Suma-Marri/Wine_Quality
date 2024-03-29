# Wine Quality

Storyboard: https://docs.google.com/presentation/d/1xI2P8KyCw7fxwQUVKRoSWpTGTt67C00HO_zXt9kASmo/edit#slide=id.g12ec38b41d9_0_64

## Project Overview

#### Selected topic: Wine Quality Prediction

Here we will predict the quality of wine on the basis of giving features. We are using the wine quality dataset from Kaggle. This dataset has the fundamental features that are responsible for affecting the quality of the wine. By the use of several Machine learning models, we will predict the quality of the wine.

#### Technologies used

- Python
- Jupyter Notebooks
- Numpy
- Pandas 
- Matplotlib
- Tableau
- JavaScript
- scikit-learn 


#### Reason why we selected this topic: 

We had a similar interest in wine and were curious on which characteristics of wine affect its quality. We also want to predict what kind of wines could possibly win certain wine competitions.  

#### Description of the source of data: 

##### _RedWine_dataset.csv_ and _WhiteWine_dataset.csv_

We found a dataset to start with that has multiple features for different kinds of wines, such as pH and density. 
  - https://www.kaggle.com/rajyellow46/wine-quality
  - https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/

Dataset description: These are the names of Features from the datasets.

_Input Variables_

- Fixed acidity: The predominantly fixed acids in wine, such as tartaric, succinic, citric, and malic acids.
- Volatile acidity: The high acetic acid present in wine, which causes an unpleasant vinegar taste.
- Citric acid: A weak organic acid used to increase the freshness and flavor of the wine.
- Residual sugar: The amount of sugar left after fermentation.
- Chlorides: The amount of salt in wine. The lower chloride rate creates better-quality wines.
- Free sulfur dioxide: SO2 is used to prevent wine from oxidation and microbial spoilage.
- Total sulfur dioxide: The amount of free and bound forms of SO2.
- Density: Depends on the alcohol and sugar content. Better wines usually have lower densities.
- pH: Used to check the level of acidity or alkalinity of wine.
- Sulphates: An antibacterial and antioxidant agent added to the wine.
- Alcohol: The percentage of alcohol in wine. A higher concentration leads to better quality.

_Output Variable_

- Quality score: The quality rating of wine that is based on sensory data and scores from 0 to 10. 

##### _PortugueseWineReviews.csv_
Dataset description: This csv file has all the reviews from BlogOsVinhos. The alcohol is measured by percentage. The prices are in euros (€). The rating is between 0-20. Sadly, so of the columns are in Portuguese, like the Judge's notes and the dates, but luckily we have Google Translate! There are some missing values, which were replaced with -1 (for numerical values) and null (for non-numerical values). Just in case the extraction did not pick up the values, there is a link column in case if you want to research and replace and null/-1 values. Also, there are wines available in Portugal, not made in Portugal, although some of them are made in Portugal. 

#### _Wine Enthusiast reviews_ 

Data set description: From a previous scrape multiple files containing 250k reviews from wine enthusiast magazines were joined together and filtered between Portuguese red wines and Portuguese white wines. All nonrelevant information was removed like wine subregions, winery, and wine name. For our study price and rating are the most relevant. Using this information we hope to compare it with the Machine learning model and check its efficiency.

_Input Variables_

- Name: Name of the wine
- Year: Year of the wine
- Region: Region where the wine product was grown.
- Color: Color of wine
- Castes: Caste/Classification of the wine
- AlcoholPercentage: The alcohol content measured by the percentage
- Producer: The producer of the wine.
- MinimunPrice: Minimum price of a bottle.
- MaximumPrice: Maximum price of a bottle.
- Judge: Judge's name
- JudgeRating: Judge's rating between 0-20
- Date: Judge put in a review.
- JudgeNotes: The commentary the judge put about the wine.
- Label: Label of the wine bottle.
- Link: Link to the review on BlogOsVinhos.
 

#### Questions that we hope to answer with the data: 

- We hope to find out what makes certain wines have a higher quality than others. 
- Which wines have better quality for less monetary value 
- Which styles of wines have the highest ratings

####  Description of the communication protocols

The group kept discussing the project details during live sessions and constantly making contact with each other through the Slack app, including sharing information and data that we found online.

## Machine Learning FlowChart

### DataSet
Wine Quality DataSet

### What type of input data?
* Label: Type
* Classification: fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free sulfur dioxide, total sulfur dioxide, density, pH, sulfates, alcohol
* Large number of variables: N/A
* Non-tabular: N/A

### What type of data cleaning?
* Remove any values that have null or undefined values. If there are any values missing in a particular column, we might drop it. If we see that a particular wine has a high/low quality with a missing value, such as pH. We can possibly predict the pH by comparing to other records with similar chemical make-up and do additional research in order to potentially add a new accurate value for the missing cell.
* Remove any columns that don't affect the wine quality. For example, residual sugars and chlorides don't seem to affect the quality of wine, considering they have a low correlation between both variables, we would drop these two columns.
* Sometimes, the wine names have special characters, which might not be able to pass through Jupyter Notebook, and when downloaded or uploaded as a CSV, information might be lost. To avoid this, I plan to change some of the special names so that they can pass through Jupyter Notebook without any errors. I will also add a unique ID number so that we can easily match the wines at the end.

### Feature Engineering Required?
 ### Additions to the DataSet
* Wine types (White, Red) 
* Styles (Sparkling, Light-Bodied White, Full-Bodied White, Light-Bodied Red, Full-Bodied Red, Dessert, Rosé, etc.)
* List Price

### What is the Machine Learning Model?
* Supervised Machine Learning

### How are you evaluating and testing the Machine Learning model?
* Linear Regression Model

## Database

#### Database sample

* By using the wine quality database provided on the top of the document and other wine rating apps information three new variables will be added to the list: Wine Type, style & price list. The final database will be developed using PostgreSQL.

The expected database should be similar to this example:
![alt text](https://github.com/ramonmhung/Resources/blob/main/Screen%20Shot%202022-05-08%20at%2010.49.38%20AM.png)

## Machine Learning

#### *Description of preliminary data preprocessing*
* The preliminary data is the ‘Wine Quality’ dataset from Kaggle, which was downloaded from the UCI Machine Learning Repository. The dataset is related to red and white variants of the Portuguese "Vinho Verde" wine. The input variables of the data include these stats: fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, and alcohol. The output/ target variable is ‘quality’. Before the data was imported into Jupyter Notebook to begin the Machine Learning, we first divided the dataset into two CSV files; Red Wine and White Wine

#### *Description of preliminary feature engineering and preliminary feature selection, including the decision-making process*
* All the variables within the entire dataset are qualitative, so no columns or rows need to be dropped. Further cleaning of the dataset found that there were 240 duplicates out of 1599 which needed to be dropped. After this, a heat map was created to visualize correlations between variables. There were strong correlations between alcohol and quality, density and fixed acidity, fixed acidity, and citric acid, which gives a more focused group of input variables to pass through our machine learning model.

#### *Description of how data was split into training and testing sets*
* For the splitting of the data into testing and training sets was done by first importing necessary dependencies including 'train_test_split'. 'LinearRegression' and 'metrics' from the Scikit-learn library. The numpy random seed value is set to 0 in order to provide the starting input for NumPy's pseudo-random number generator. Training and testing sets were then created with 75% of the data used for training and the remaining 25% for testing. The target variable (y) was set to 'quality' from the red_wine data frame.

#### *Explanation of model choice, including limitations and benefits*
* Linear Regression is the primary model chosen. As supervised learning is well suited to input and output variables to predict outcomes - in our case the relationship between quality and numerous input variables - the regression model is expected to perform efficiently and give us an accurate and simple visualization of the data. A limitation within the dataset is that there were only 12 initial attributes in the dataset, and based on the correlation heatmap, we must limit our model to variables that have high correlations. 

## Dashboard

Link (local): http://127.0.0.1:5000

#### Tools used to create the final Dashboard:

### JavaScript, HTML/CSS

These are used to create an interactive webpage, where the user can input the values for the various wine features and then on the click of the button (‘Predict’), the quality of the wine is displayed in the form of a text message.

<img width="590" alt="Screen Shot 2022-05-18 at 8 24 11 PM" src="https://user-images.githubusercontent.com/95826875/169367488-062e39e6-9224-418c-9204-39d847352322.png">
<img width="590" alt="Screen Shot 2022-05-29 at 10 26 29 AM" src="https://user-images.githubusercontent.com/95826875/170874688-cd605c55-c024-4640-8159-7edf4b876f13.png">
<img width="622" alt="Screen Shot 2022-05-29 at 10 36 12 AM" src="https://user-images.githubusercontent.com/95826875/170874906-7428f72b-22dc-439d-9397-7c354020df44.png">
<img width="659" alt="Screen Shot 2022-06-01 at 3 12 22 PM" src="https://user-images.githubusercontent.com/95826875/171483781-7a5c0644-3019-4557-b65c-a73036171b2e.png">
<img width="664" alt="Screen Shot 2022-06-01 at 3 11 52 PM" src="https://user-images.githubusercontent.com/95826875/171483814-a681c6d7-550b-4df4-b651-ab64adef6f0c.png">


### Tableau

Tableau is used to create different visualizations showing correlations between wine features vs the quality of wine.
On the webpage, there’s a tab ‘Dashboard’ which upon clicking navigates to another page where the Wine Dashboard is presented with two different tableau dashboards for Red Wine and White Wine Quality Analysis.

<img width="362" alt="Screen Shot 2022-06-01 at 11 21 53 AM" src="https://user-images.githubusercontent.com/95826875/171440657-83333a18-5dd0-4714-b4eb-a305d24e30a7.png">


#### Tableau Dashboards

- Red Wine Quality Analysis

https://public.tableau.com/app/profile/surbhi.bawaria/viz/RedWineQualityAnalysis_16527286095740/RedWineQualityAnalysis

- White Wine Quality Analysis

https://public.tableau.com/app/profile/surbhi.bawaria/viz/WhiteWineQualityAnalysis/WhiteWineQualityAnalysis






