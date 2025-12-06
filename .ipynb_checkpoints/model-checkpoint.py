import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay


df = pd.read_csv('data/churn.csv')

def model_factory(model, columns):
    """
    Creator: Daniel
    inputs: 
        model: The machine learning model object to use in the pipeline
        columns: the list of columns to use for scaling
    outputs:
        returns the model, ready to be fitted and used. 
    """
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), columns)
        ],
        remainder='passthrough'
    )
    # this preprocessor will scale the columns passed in. Any other columns will go through without being scaled. 
    model = Pipeline(
        steps=[
            ('preprocess', preprocessor),
            ('model', model)
        ]
    )
    # this is the pipeline the model will use, so it will first scale it with the preprocessor, then run it through the model. 
    # this will make it easier to use, as it will scale the inputs automatically, so it doesn't need to be scaled
    # outside of the model. 
    return model


"""
Model performance testing was done in classification.ipynb
where it was found that Random Forest model 
and a split of 0.28 performed the best. 
For more information, see classification.ipynb.
"""




cols = ['day_charge', 'eve_charge', 'night_charge', 'intl_charge', 'custserv_calls']
# columns used for modeling

X = df[cols]
# independent features
y = df['churn']
# target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.28, random_state=42, stratify=y)
    
rf = model_factory(RandomForestClassifier(random_state=42), X.columns)

rf.fit(X_train, y_train)

# with open('model.pkl', 'wb') as file:
#     pickle.dump(rf, file)








