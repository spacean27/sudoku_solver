# sudoku_solver
This Project aims to solve complex sudoku problems for sudoku time-attackers.  
The solver is made with Integer Linear Programming.  
There are 3 problems for each level. Just 1 problem will be selected randomly when you run the code.  

## for Users
### Web Application
coming soon

## for Developers
### Documentation
coming soon

### Data
All users are allowed to implement user-made sudoku problems in csv format.  
1. Place your own sudoku problems to `/dataset/user` directory.  
2. Please do NOT forget to change the `--level` parameter when you run the code.

### How to build environment
1. Install poetry from [here](https://python-poetry.org/docs/#installation).
2. Run `poetry shell` in your terminal.
3. Run `poetry install` in your terminal.

### How to run
1. **Preprocess:** `python preprocess.py --level {easy/medium/hard/user}` default: --level easy.  
2. **Solve:** `python solve.py --level {easy/medium/hard/user}` default: --level easy.  
3. **Postprocess:** `python postprocess.py --level {easy/medium/hard/user}`.  
- You do not have to run preprocess.py before running solve.py to solve a sudoku problem.  
- solve.py also runs preprocess.py.  
- postprocess does not work yet.  

If you would like to run all scripts at the same time, here is an alternative way.  
- `python run_all.py`  
- This does not work yet.  

**You can run to solve a sudoku problem only with** `python solve.py --level {easy/medium/hard/user}` **just for now.**
