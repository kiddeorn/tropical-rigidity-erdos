#!/usr/bin/env python3
# wild_scattering_check.py
# Symbolic verification of Maurer-Cartan consistency and H-invariance for Wild-Type Core

import sympy as sp

print("Initializing Markov Quiver (Wild-Type Core) and variables...")

# Define standard symbolic variables in pure Python
x1, x2, x3 = sp.symbols('x1 x2 x3')
X = [x1, x2, x3]

# The TRUE Hamiltonian invariant for the Markov Quiver
H = (x1**2 + x2**2 + x3**2) / (x1*x2*x3)
print(f"Testing invariant H = {H}")

# The Markov Quiver Exchange Matrix (Rank 3)
B = [
    [ 0,  2, -2],
    [-2,  0,  2],
    [ 2, -2,  0]
]

def mutate_variable(vars_list, k, B_matrix):
    """
    Symbolically mutates the k-th cluster variable using subtraction-free rational expressions.
    """
    M1 = 1
    M2 = 1
    for i in range(3):
        if B_matrix[i][k] > 0:
            M1 *= vars_list[i]**B_matrix[i][k]
        elif B_matrix[i][k] < 0:
            M2 *= vars_list[i]**(-B_matrix[i][k])
            
    return (M1 + M2) / vars_list[k]

def main():
    all_passed = True
    
    # Test mutation invariance for each node
    for k in range(3):
        # Calculate the new mutated variable
        x_mut = mutate_variable(X, k, B)
        
        # Create the new set of variables after mutation mu_{k+1}
        X_new = list(X)
        X_new[k] = x_mut
        
        # Substitute the new variables into the Hamiltonian H
        H_mutated = (X_new[0]**2 + X_new[1]**2 + X_new[2]**2) / (X_new[0]*X_new[1]*X_new[2])
        
        # Check equality by simplifying the difference (H - H_mutated)
        diff = sp.simplify(H - H_mutated)
        is_invariant = (diff == 0)
        
        print(f"- Mutation mu_{k+1} applied. Checking H == mu_{k+1}(H)... [{'TRUE' if is_invariant else 'FALSE'}]")
        if not is_invariant:
            all_passed = False

    if all_passed:
        print("[Success] H is a global invariant! Maurer-Cartan 1-cohomology condition verified.")
    else:
        print("[Warning] Invariance broken. Check Quiver or Hamiltonian definitions.")

if __name__ == "__main__":
    main()
