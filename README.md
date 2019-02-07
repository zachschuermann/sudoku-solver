# Sudoku Solver
CLI Sudoku solver implemented in python with the python API for Z3 SMT solver.

## Install
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
$ python -m unittest sudoku
```

## Distributing
```bash
$ python setup.py sdist bdist_wheel
```
