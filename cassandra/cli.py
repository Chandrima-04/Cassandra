import pandas as pd
import numpy as np
import os.path
import click
from random import randint

from .preprocessing import (
    parse_raw_data,
    parse_feature,
    normalize_data,
)

from .prediction import (
    prediction_methodology
)

@click.group()
def main():
    pass


@main.command('predict')
@click.option('--feature-name', default='Location',
               help='The feature to predict on')
@click.option('--accuracy', default=0.75,
               help='Desired accuracy for the model')
@click.option('--test-size', default=0.2,
              help='The relative size of the test data')
@click.option('--num-estimators', default=20,
              help='Number of trees in our random forest')
@click.option('--num-runs', default=1000, help='Number of random forest runs')
@click.option('--num-data', default=50,
              help='Number of top data variables to be predicted')
@click.option('--normalize-method', default='standard_scalar',
              help='Normalization method to be used')
@click.option('--normalize-threshold', default='0.0001',
              help='Normalization threshold for binary normalization.')
@click.argument('data-file', type=click.File('r'))
@click.argument('metadata-file', type=click.File('r'))
@click.argument('out-dir')
def predict_top_features(feature_name, accuracy, test_size, num_estimators, num_runs,
                         num_data, normalize_method, normalize_threshold,
                         data_file, metadata_file, out_dir):
    """Train a random-forest model to predict the top data variables."""
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    raw_data, microbes = parse_raw_data(data_file)
    seed = randint(0, 500)
    feature, name_map = parse_feature(metadata_file, raw_data.index, feature_name=feature_name)
    new_index = feature!= -1
    raw_data = raw_data[new_index == True]
    feature = feature[new_index == True]
    normalized = normalize_data(raw_data, method=normalize_method, threshold=normalize_threshold)
    print ("Shape of dataset after normalization", normalized.shape)
    top_features_rf, model_parameters_rf = prediction_methodology(
                                     normalized, feature,
                                     microbes, accuracy=accuracy, num_runs=num_runs, num_data=num_data,
                                     test_size=test_size, num_estimators=num_estimators, seed=seed)
    top_features_rf.to_csv(os.path.join(out_dir, str('top_data_feature_rf_' + normalize_method + '.csv')))
    model_parameters_rf.to_csv(os.path.join(out_dir, str('model_parameters_rf_' + normalize_method + '.csv')))

if __name__ == '__main__':
    main()
