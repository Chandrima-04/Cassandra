# Cassandra

Cassandra is a package for performing factor analysis for sparse datasets. Designed for metagenomics data, it can also be used in other types of datasets including single-cell, or any other sparse dataset. 

Machine Learning algorithms usually act like a black-box, thus what is happening in prediction using an ML algorithm is difficult to know. Some known issues of using ML in metagenomics datasets are due to their structure which includes:
- Quantatitive: Metagenomic results are usually quantative. Based on the tool they can be absolute or relative values in a given sample
- Categorical: Variables represent types of data which may be divided into groups
- Nominal: Data that is classified without a natural order or rank
- Unbalanced: Most of the dataset are usually unbalanced in nature
- Compositional: Compositional data are quantitative descriptions of the parts of some whole, conveying relative information
- Non-normal and not-Gaussian and not-Bayesian model: Does not follow any distribution pattern
- Sparse Datasets: Most of the value in an matrix are 0
- Usually m>n where m= number of microbes and n=number of samples

Cassandra (Greek Mythology: Trojan Priestess of Apollo known for her prophecies) is a tool to envisage potential microbial factors influencing the ML tool based on features. Many times we find the top abundant microbes are not the indicator species. Hence, using Random Forest, we try to determine the indicator species responsible as a differential factors across environments.

## Preprocessing
Following are the preprocessing methods Cassandra allows to accomodate the needs of metagenomics data:
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

## Requirements

- Python >= 3.6
- Cython
- scikit-learn
- scikit-bio
- numpy
- pandas
- scipy
- click

## Usage

```
cassandra predict --feature-name <Metadata-factor> ...  <input> <meta-data> <output>
```

The parameters and their default value is mentioned below. All parameters can be set. When the parameters are chosen, the default is updated as per the user input.

```
  --accuracy FLOAT            Desired accuracy for the model to achieve. Default=0.75
  --test-size FLOAT           The relative size of the test data. 0.2
  --num-estimators INTEGER    Number of trees in our Ensemble Methods. Default=20
  --num-runs INTEGER          Number of random forest runs with user selected accuracy for finding bioindicator species. Default=1000
  --num-data INTEGER          Number of top data microbes based on the run to be output. Default=50
  --normalize-method TEXT     Normalization method selected for preprocessing. Default=standard_scalar
  --feature-name TEXT         The feature to be used, mostly geolocation. Default=city
  --normalize-threshold TEXT  Normalization threshold for binary normalization. Default=0.0001
  input CSV_FILE              Input file consisting of species (OTU/WGS/Nanopore data) for multiple samples
  meta_data CSV_FILE          additional information about sample, feature name should consist of a column name from this file
  output FOLDER               name of the folder in which the output file will be generated
```

For more options

```
cassandra --help
```


### Example 

```
cassandra predict --feature-name city --accuracy 0.80 toy_data/toy_input.csv toy_data/toy_metadata.csv toy_data/toy_output
```


## Output

The output folder consist two files:
- model_parameters_rf_normalization_method.csv


```
Accuracy            The accuracy for the given run 
Precision           Precision for the given run
Recall              Recall value for the given run
Microbe_name        The weight associated with the microbe for the given run
```

- top_data_feature_rf_normalization_method.csv: Consist the top n features (microbes in metagenomics data) along with the weight associated with those features. (Default: 50, can be modified)


## Datasets

The datasets used in this Paper are from 

- MetaSUB: Danko, D., Bezdan, D., Afshin, E.E., Ahsanuddin, S., Bhattacharya, C., Butler, D.J., Chng, K.R., Donnellan, D., Hecht, J., Jackson, K. and Kuchin, K., 2021. A global metagenomic map of urban microbiomes and antimicrobial resistance. Cell, 184(13), pp.3376-3393.

- TARA Ocean: Salazar, G., Paoli, L., Alberti, A., Huerta-Cepas, J., Ruscheweyh, H.J., Cuenca, M., Field, C.M., Coelho, L.P., Cruaud, C., Engelen, S. and Gregory, A.C., 2019. Gene expression changes and community turnover differentially shape the global ocean metatranscriptome. Cell, 179(5), pp.1068-1083.

## License

All material is provided under the MIT License.

## Credits

This package is written and maintained by [Chandrima Bhattacharya](mailto:chb4004@med.cornell.edu).

