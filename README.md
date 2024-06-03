
# Parametrization

Parametrization that takes the radius of a sphere and return its volume

## Install it from PyPI

```bash
pip install -i https://test.pypi.org/simple/ parametrization==0.0.3
```

## Usage

### Local environment
```py
from parametrization.core import calculate_volume
calculate_volume(arg)
```
#### CLI (locally within the directory)
```bash
$ python -m parametrization.cli [arg]
```

#### Docker
```bash
docker build -t parametrization .
docker run parametrization [numerical arg]
```



