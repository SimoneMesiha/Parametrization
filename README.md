# Parametrization

Parametrization is a Python package that calculates the volume of a sphere given its radius. It provides both a programmatic interface and a command-line interface (CLI) for ease of use.

## Features

- Calculate the volume of a sphere given its radius.
- Easy-to-use CLI for quick calculations.
- Docker support for running the package in isolated environments.

## Installation

### From PyPI

Install the package from PyPI (TestPyPI for version 0.0.3):

```bash
pip install -i https://test.pypi.org/simple/ parametrization==0.0.3
```

### From Source

```bash
git clone https://github.com/SimoneMesiha/Parametrization.git
cd parametrization
pip install .
```

## Usage
```py
from parametrization.core import calculate_volume
# Replace 'arg' with a positive numerical value
calculate_volume(arg)
```
#### CLI (locally within the directory)
```bash
#Replace arg with a positive numerical value
$ python -m parametrization.cli [arg]
```

#### Docker
```bash
docker build -t parametrization .
docker run parametrization [numerical arg]
```

## Contribution guidelines
1. Clone the repository and create a new branch for your feature
2. commit and push your changes
4. Make sure your changes don't break any test (see below how to run tests)
5. create a pull request to main repository


## Running tests
```bash
 python -m unittest discover -s parametrization/test
```



