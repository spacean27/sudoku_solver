# sudoku_solver
This Project solves complex sudoku problems for sudoku time-attakers.

## for Users
### Web Application
coming soon

## for Developers
### Documentation
coming soon

### Data
coming soon

### How to build environment
1. Install poetry from [here](https://python-poetry.org/docs/#installation).
2. Run `poetry shell` in your terminal.
3. Run `poetry install` in your terminal.

### How to run
1. **Preprocess:** `python preprocess.py`.  
2. **Solve:** `python solve.py --level {easy/medium/hard}`.  
You do not have to run preprocess.py before running solve.py to solve a sudoku problem.  
solve.py also runs preprocess.py.

If you would like to run all scripts at the same time, here is an alternative way.  
- `python run_all.py`
