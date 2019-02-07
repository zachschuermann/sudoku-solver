# Sudoku Solver
[![Build Status](https://img.shields.io/travis/com/schuermannator/sudoku-solver.svg?style=flat-square)](https://travis-ci.com/schuermannator/sudoku-solver)
[![Coverage Report](https://img.shields.io/coveralls/github/schuermannator/sudoku-solver.svg?style=flat-square)](https://coveralls.io/github/schuermannator/sudoku-solver)
[![PyPI Status](https://img.shields.io/pypi/v/sudoku-solve.svg?colorB=blue&style=flat-square)](https://pypi.org/project/sudoku-solve/)

CLI Sudoku solver implemented in python with the python API for Z3 SMT solver.

## Install and Run
```bash
$ pip install sudoku-solve
$ sudoku-solve 
```
#### Supports Input Redirection
```bash
$ sudoku-solve < puzzle.txt
```

## Building
```bash
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

## Run
```bash
$ python sudoku.py
```
or with input from a file: 
```bash
$ python sudoku.py < test.txt
```

## Test
```bash
$ python -m unittest sudoku_solve.sudoku
```

## Distributing
```bash
$ python setup.py sdist bdist_wheel
$ python -m twine upload dist/*
```
