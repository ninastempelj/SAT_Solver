# SAT_Solver
**Authors: Nina Štempelj and Urša Pertot**

This repository contains our version of a SAT Solver, that we created as part of our course on Logic in computer science.

As input it takes a [DIMACS file](http://people.sc.fsu.edu/~jburkardt/data/cnf/cnf.html). How it work is nicely seen by running the Solver on file _"testGraph.txt"_, that can be found in the repository.
If the formula is satisfiable it prints the valuation in the output text file, otherwise it print a single 0 in the output text file.

You can run the SAT Solver by running the file Solver.py and calling the function `main("input_file.tex", "output_file.txt")`
It can also be run from command line: `python Solver.py "input_file.txt" "output_file.txt"`. In addition to producing an output file containing the solution, it will also print the solution in the command prompt.

In addition to the SAT Solver the repository contains folders Examples and Graphs with a few easy examples of DIMACS files and their solutions. The file `sudoku2DIMACS.py` converts sudoku problems to DIMACS files and the file `GraphGenerator.py` creates random graph colouring problems (in DIMACS format).
