# PAC2020-RPS

![Python application](https://github.com/shin-sforzando/PAC2020-RPS/workflows/Python%20application/badge.svg)
[![codecov](https://codecov.io/gh/shin-sforzando/PAC2020-RPS/branch/master/graph/badge.svg)](https://codecov.io/gh/shin-sforzando/PAC2020-RPS)

Python Ability Check 2020: Rock-paper-scissors

- [Requirements](#requirements)
- [How to Run](#how-to-run)
  - [Create Virtual Environment](#create-virtual-environment)
  - [Install Dependencies](#install-dependencies)
  - [Run](#run)
  - [Lint](#lint)
  - [Test](#test)
  - [Clean](#clean)
- [References](#references)
- [Miscellaneous](#miscellaneous)

## Requirements

- Python 3.8.5 or higher
  - [pytest](https://docs.pytest.org/en/stable/)
    - [pytest-cov](https://pypi.org/project/pytest-cov/)
  - [flake8](https://pypi.org/project/flake8/)
    - [hacking](https://github.com/openstack/hacking)
  - [tqdm](https://github.com/tqdm/tqdm)

## How to Run

### Create Virtual Environment

```shell
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```shell
make upgrade
```

### Run

```shell
python main.py
```

### Lint

```shell
make lint
```

### Test

```shell
make test
```

### Clean

```shell
make clean
```

## References

- [Strategy パターン - Wikipedia](https://ja.wikipedia.org/wiki/Strategy_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3)

## Miscellaneous

- [Python Ability Check 2020 - HackMD](https://hackmd.io/@sfz/BkoJEGOGD)
