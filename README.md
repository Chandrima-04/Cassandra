# Cassandra

Cassandra is a package for performing factor analysis for sparse datasets. Designed for metagenomics data, it can also be used in other types of datasets including single-cell, or any other sparse dataset. 

Machine Learning algorithms usually acts like a black-box, thus what is happening in prediction using an ML algorithm is difficult to know. Some known issues of using ML in metagenomics datasets are due to the structur of metagenomic dataset which includes:
- Quantatitive: Metagenomic results are usually quantative. Based on the tool they can be absolute or relative values in a given sample.
- Categorical: Variables represent types of data which may be divided into groups
- Nominal: Data that is classified without a natural order or rank
- Unbalanced: Most of the dataset are usually unbalanced in nature
- Compositional: Compositional data are quantitative descriptions of the parts of some whole, conveying relative information
- Non-normal and not-Gaussian and not-Bayesian model: Does not follow any distribution pattern
- Sparse Datasets: Most of the value in an matrix are 0
- Usually m>n where m= number of microbes and n=number of samples

Cassandra (Greek Mythology: Trojan Priestess of Apollo known for her prophecies) is a tool to envisage potential microbial factors influencing the ML tool based on features. Many times we find the top abundant microbes are not the indicator species. Hence, using Random Forest, we try to determine the indicator species responsible as a differential factors across environments.

Following are the preprocessing methods Cassandra allows:
- binary: 0,1 based on a threshold value (default=0.0001)
- clr: transformation function for compositional data based on Aitchison geometry to the real space
- multiplicative_replacement: transformation function for compositional data  uses the multiplicative replacement strategy for replacing zeros such that compositions still add up to 1
- raw: no preprocessing
- standard scalar: forces the column to have a mean of 0
- total-sum: relative abundance method having the sum of each row to be 1

NOTE: Multiple methods of transformation/preprocessing will distort the data.

![Cassandra](https://user-images.githubusercontent.com/9072403/177629034-8f2df5e0-3ffb-4554-ab49-5577cb9392cb.jpeg)


## Installation

From source
```
git clone https://github.com/Chandrima-04/Cassandra.git
cd Cassandra
python setup.py install
```

## Usage

```
cassandra predict --feature-name <Metadata-factor> ...  <input> <meta-data> <output>
```


### Example 

```
cassandra predict --feature-name city --accuracy 0.80 toy_data/toy_input.csv toy_data/toy_metadata.csv toy_data/toy_output
```

Parameters include:

```
  --accuracy FLOAT            Desired accuracy for the model
  --test-size FLOAT           The relative size of the test data
  --num-estimators INTEGER    Number of trees in our Ensemble Methods
  --num-runs INTEGER          Number of random forest runs
  --num-data INTEGER          Number of top data variables to be predicted
  --normalize-method TEXT     Normalization method
  --feature-name TEXT         The feature to predict
  --normalize-threshold TEXT  Normalization threshold for binary normalization
  input CSV_FILE              Input file consisting of species (OTU/WGS/Nanopore data) for multiple samples
  meta_data CSV_FILE          additional information about sample, feature name should consist of a column name from this file
  output FOLDER               name of the folder in which the output file will be generated
```


## Output

The output folder consist two files:
- model_parameters_rf_normalization_method.csv


```
Accuracy	        The accuracy for the given run 
Precision	        Precision for the given run
Recall            Recall value for the given run
Microbe_name      The weight associated with the microbe for the given run
```

- top_data_feature_rf_normalization_method.csv: Consist the top n features (microbes in metagenomics data) along with the weight associated with those features. (Default: 50, can be modified)

## License

All material is provided under the MIT License.

## Credits

This package is written and maintained by [Chandrima Bhattacharya](mailto:chb4004@med.cornell.edu).

