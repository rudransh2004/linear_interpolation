def linear_interpolation(eq_function, A, B, n_iterations=5, tolerance=1e-6):
    results = []
    previous_xn = None
    
    for n in range(1, n_iterations+1):
        fA = eq_function(A)
        fB = eq_function(B)
        
        xn = (A * fB - B * fA) / (fB - fA)
        fxn = eq_function(xn)
        
        results.append({
            'n': n,
            'A_n': A,
            'f(A_n)': fA,
            'B_n': B,
            'f(B_n)': fB,
            'x_n': xn,
            'f(x_n)': fxn
        })

        if previous_xn is not None and abs(xn - previous_xn) < tolerance:
            print("Converged!")
            break
        
        if fA * fxn < 0:
            B = xn
        else:
            A = xn
        
        previous_xn = xn
    else:
        print("Warning: Method did not converge in the given number of iterations!")

    return results

def pretty_print(results):
    print("n\tA_n\tf(A_n)\tB_n\tf(B_n)\tx_n\tf(x_n)")
    print("-" * 70)
    for row in results:
        print(f"{row['n']}\t{row['A_n']:.5f}\t{row['f(A_n)']:.5f}\t{row['B_n']:.5f}\t{row['f(B_n)']:.5f}\t{row['x_n']:.5f}\t{row['f(x_n)']:.5f}")


