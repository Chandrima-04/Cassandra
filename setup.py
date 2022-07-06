import setuptools

requirements = [
    'scikit-learn==0.24.1',
    'numpy',
    'pandas',
    'scipy',
    'click',
    'scikit-bio',
]


setuptools.setup(
    name="Cassandra",
    version="0.1.0",
    url="https://github.com/Chandrima-04/Cassandra",
    author="Chandrima Bhattacharya",
    author_email="cb4603@nyu.edu",
    description="Predict top contributors for sample distinction",
    packages=setuptools.find_packages(),
    package_dir={'cassandra': 'cassandra'},
    entry_points={
        'console_scripts': [
            'cassandra=cassandra.cli:main',
        ]
    },
    install_requires=requirements,
)
