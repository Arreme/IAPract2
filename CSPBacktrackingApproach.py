from aima3 import csp
import random
##OUR PROBLEM:

class Tafur(csp.CSP):
    def __init__(self):
        csp.CSP.__init__(self, variables, domains, neighbors, self.differentTypeCard)

    def display(self, assignment):
        print('0: ',assignment[0],' | 1:', assignment[1],' | 2:',assignment[2])
        print('3: ',assignment[3] ,' | 4:', assignment[4],' | 5:', assignment[5])
        print('6: ',assignment[6],' | 7:',assignment[7],' | 8:', assignment[8])
    
    def differentTypeCard(self, A, a, B, b):
        
        return int(a/10) != int(b/10)
    
    def suppose(self, var, value):
        """Start accumulating inferences from assuming var=value."""
        self.support_pruning()
        removals = [(var, a) for a in self.curr_domains[var] if a != value]
        if self.curr_domains is not None:
            for key in self.curr_domains:
                if var != key and value in self.curr_domains[key]:
                    removals.append((key,value))
        self.curr_domains[var] = [value]
        return removals

    def nconflicts(self, var, val, assignment):
        """Return the number of conflicts var=val has with other variables."""
        # Subclasses may implement this more efficiently
        def conflict(var2):
            return (var2 in assignment and
                    not self.constraints(var, val, var2, assignment[var2]))
        
        nConflics = count(conflict(v) for v in self.neighbors[var])
        
       
        return nConflics


var = [11,12,13,21,22,23,31,32,33]
random.shuffle(var)
domains = {0:[var[0]],1:var[1:],2:var[1:],
           3:var[1:],4:var[1:],5:var[1:],
           6:var[1:],7:var[1:],8:var[1:]}

variables = [0,1,2,3,4,5,6,7,8]

neighbors = {0: {1,2},1: {0,2},2: {0,1},
             3: {4,5},4: {3,5},5: {3,4},
             6: {7,8},7: {6,8},8: {6,7}}

             
def mrv(assignment, csp):
    """Minimum-remaining-values heuristic."""
    row1 = 0
    row2 = 0
    row3 = 0
    if len(list(assignment.keys()))==0:
        return 0
        
    for keys in assignment.keys():
        if keys in [0,1,2]:
            row1 += 1  
        elif keys in [3,4,5]:
            row2 += 1
        elif keys in [6,7,8]:
            row3 += 1
    possibles = []
    if not(row1-row2 >= 1 or row1 - row3 >= 1):
        possibles.append(0)
        possibles.append(1)
        possibles.append(2)
    if not(row2-row1 >= 1 or row2 - row3 >= 1):
        possibles.append(3)
        possibles.append(4)
        possibles.append(5)
    if not(row3-row1 >= 1 or row3 - row2 >= 1):
        possibles.append(6)
        possibles.append(7)
        possibles.append(8)
    random.shuffle(possibles)
    return possibles[0]
    

def forward_checking(csp, var, value, assignment, removals):
    """Prune neighbor values inconsistent with var=value."""
    for B in csp.neighbors[var]:
        if B not in assignment:
            for b in csp.curr_domains[B][:]:
                if not csp.constraints(var, value, B, b):
                    csp.prune(B, b, removals)
            if not csp.curr_domains[B]:
                return False
    
    for key in csp.curr_domains:
        if var != key and value in csp.curr_domains[key]:
            csp.prune(key, value, removals)
    return True

def count(seq):
    """Count the number of items in sequence that are interpreted as true."""
    return sum(bool(x) for x in seq)

prob = Tafur()
prob.display(csp.backtracking_search(prob, select_unassigned_variable=mrv, inference=forward_checking))
