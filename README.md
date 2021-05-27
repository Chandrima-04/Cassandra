# Cassandra

Cassandra is a package for performing factor analysis for sparse datasets. Designed for metagenomics data, it can also be used in other types of datasets including single-cell, or any other sparse dataset. Based on metadata, the following package will output the top contributions in a sample.

Following preprocessing can be done:
- total-sum: samples expressed as the probabilities;
- standard scalar: forces the column to have a mean of 0;
- binary: 0,1 based on a threshold.

## Installation

From source
```
git clone git@github.com:Chandrima-04/Cassandra.git
cd Cassandra
python setup.py install
```

