# Wine Quality

### Machine Learning (DELIVERABLE 2)

#### *Description of preliminary data preprocessing*
* The preliminary data is the ‘Wine Quality’ dataset from kaggle, which was downloaded from UCI Machine Learning Repository. The dataset is related to red and white variants of the Portuguese "Vinho Verde" wine. The input variables of the data includes; fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, and alcohol. The output/ target variable is ‘quality’. Before the data was imported into Jupyter Notebook to begin the Machine Learning, we first divided the dataset into two CSV files; Red Wine and White Wine

#### *Description of preliminary feature engineering and preliminary feature selection, including the decision-making process*
* All the variables within the entire dataset are qualitative, so no columns or rows needed to be dropped. Further cleaning of the dataset found that there were 240 duplicates out of 1599 which needed to be dropped. After this, a heat map was created to visualize correlations between variables. There were strong correlations between alcohol and quality, density and fixed acidity, fixed acidity and citric acid, which gives a more focused group of input variables to pass through our machine learning model.

#### *Description of how data was split into training and testing sets*
* For the splitting of the data into testing and training sets was donw by first importing necessary dependencies including 'train_test_split'. 'LinearRegression' and 'metrics' from the Scikit-learn library. The numpy random seed value is set to 0 in order to provide the starting input for NumPy's pseudo-random number generator. Training and testing sets were then created with 75% of the data used for training and the remaining 25% for testing. The target variable (y) was set to 'quality' from the red_wine dataframe.

#### *Explanation of model choice, including limitations and benefits*
* Linear Regression is the primary model chosen. As supervised learning is well suited to input and output variables to predict outcomes - in our case the relationship between quality and numerous input variables - the regression model is expected to perform efficiently and give us an accurate and simple visualization of the data. A limitation within the dataset is that there were only 12 initial attributes in the dataset, and based on the correlation heatmap, we must limit our model to variables that have high correlations. 
