# Cassandra

Cassandra is a package for performing factor analysis for sparse datasets. Designed for metagenomics data, it can also be used in other types of datasets including single-cell, or any other sparse dataset. 

Machine Learning algorithms usually acts like a black-box, thus what is happening in prediction using an ML algorithm is difficult to know. Cassandra (Greek Mythology: Trojan Priestess of Apollo known for ger prophecies) is a tool to envisage potential microbial factors influencing the ML tool based on features. Many times we find the top abundant microbes are not the indicator species. Hence, using Random Forest, we try to determine the indicator species responsible as a differential factors across environments.

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

## Usage

```
cassandra predict --feature-name <Metadata-factor> ...  <input> <meta-data> <output>
```
