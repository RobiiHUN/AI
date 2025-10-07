from ortools.sat.python import cp_model
import math

def solve_sudoku(board):
   
    n = len(board)                 # 9
    box = int(math.isqrt(n))       # 3

    model = cp_model.CpModel()

    
    X = [[model.NewIntVar(1, n, f"x_{r}_{c}") for c in range(n)] for r in range(n)]

    
    for r in range(n):
        for c in range(n):
            if board[r][c] != 0:
                model.Add(X[r][c] == board[r][c])

    
    for r in range(n):
        model.AddAllDifferent(X[r])

    
    for c in range(n):
        model.AddAllDifferent([X[r][c] for r in range(n)])

    
    for br in range(0, n, box):
        for bc in range(0, n, box):
            model.AddAllDifferent([X[r][c]
                                   for r in range(br, br + box)
                                   for c in range(bc, bc + box)])

    
    flat = [X[r][c] for r in range(n) for c in range(n)]
    model.AddDecisionStrategy(flat,
                              cp_model.CHOOSE_FIRST,
                              cp_model.SELECT_MIN_VALUE)

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return None

    return [[solver.Value(X[r][c]) for c in range(n)] for r in range(n)]