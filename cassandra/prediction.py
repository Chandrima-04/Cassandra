import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    precision_score,
    recall_score,
    confusion_matrix,
    classification_report,
    accuracy_score,
)

def split_data(data_tbl, features, test_size=0.2, seed=None):
    """Return a tuple of length four with train data, test data, train feature, test feature."""
    return train_test_split(data_tbl, features, test_size=test_size, random_state=seed)

def train_model(data_tbl, features, n_estimators=20, seed=None):
    """Return a trained model to predict features from data."""
    classifier = RandomForestClassifier(n_estimators=n_estimators, random_state=seed)
    classifier.fit(data_tbl, features)
    return classifier

def predict_with_model(model, data_tbl):
    """Return a dictionary with evaluation data for the model on the data."""
    return model.predict(data_tbl)

def feature_importance(microbes, model):
    """Return the top features of importance as selected by Random Forest Classifier."""
    importances = model.feature_importances_
    #feature_val = sorted(zip(microbes, importances), key=lambda x: x[1], reverse=True)
    feature_val = zip(microbes, importances)
    return feature_val


def prediction_methodology(normalized, feature, microbes, num_runs,
                           num_data, test_size, num_estimators, seed):
    """Code to integrate prediction of features with model accuracy"""
    train_data, test_data, train_feature, test_feature = split_data(
        normalized, feature, test_size=test_size, seed=seed
    )
    col_names = [
        'Accuracy',
        'Precision',
        'Recall',
    ]
    model_results = pd.DataFrame(columns = col_names)
    feature_dataframe = pd.DataFrame(columns = microbes)
    for i in range (0,  num_runs):
        model = train_model(
                train_data, train_feature, n_estimators=num_estimators
    	        )
        predictions = predict_with_model(model, test_data).round()
        model_results = model_results.append({'Accuracy':accuracy_score(test_feature, predictions.round()),
                        'Precision':precision_score(test_feature, predictions, average="micro"),
                        'Recall':recall_score(test_feature, predictions, average="micro")
                        }, ignore_index = True)
        feature_list = feature_importance(microbes, model)
        for microbes_name, values in feature_list:
            feature_dataframe.loc[i, microbes_name] = values
    s = feature_dataframe.sum()
    top_features = feature_dataframe[s.sort_values(ascending=False).index[:num_data]]
    model_parameters = model_results.join(feature_dataframe, sort=False)
    return top_features, model_parameters
    
