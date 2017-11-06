# SAT_Solver
**Authors: Nina Štempelj and Urša Pertot**

This repository contains our version of a SAT Solver, that we created as part of our course on Logic in computer science.

As input it takes a [DIMACS file](http://people.sc.fsu.edu/~jburkardt/data/cnf/cnf.html). If the formula is satisfiable it prints the valuation in a text file found in a folder Examples.

You can run the SAT Solver by running the file Solver.py and calling the function `main(input_file, output_file)`
It can also be run from command line : `python Solver.py input_file output_file`. In addition to producing an output file containing the solution, it will also print the solution in the command prompt.
