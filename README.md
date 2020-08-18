# PAC2020-RPS

![Python application](https://github.com/shin-sforzando/PAC2020-RPS/workflows/Python%20application/badge.svg)

Python Ability Check 2020: Rock-paper-scissors

- [Requirements](#requirements)
- [How to Run](#how-to-run)
  - [Create Virtual Environment](#create-virtual-environment)
  - [Install Dependencies](#install-dependencies)
  - [Run](#run)
  - [Lint](#lint)
  - [Test](#test)
- [References](#references)
- [Miscellaneous](#miscellaneous)

## Requirements

- Python 3.8.5 or higher
  - pytest
    - pytest-cov
  - flake8
    - hacking
  - tqdm

## How to Run

### Create Virtual Environment

```shell
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```shell
pip install -r requirements.txt
```

### Run

```shell
python main.py
```

### Lint

```shell
flake8 . --config .flake8
```

### Test

```shell
pytest -vv --durations=0 --cov . --cov-config .coveragerc --cov-report term-missing
```

## References

- [Strategy パターン - Wikipedia](https://ja.wikipedia.org/wiki/Strategy_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3)

## Miscellaneous

(T. B. D.)
