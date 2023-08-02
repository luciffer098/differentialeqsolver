import streamlit as st
import sympy as sp

def format_latex(expression):
    # Format the expression in LaTeX with proper fraction representation
    latex_str = sp.latex(expression)
    latex_str = latex_str.replace("frac", "dfrac")  # Use 'dfrac' for proper fraction representation
    return latex_str

def solve_differential_eq(differential_eq_str):
    try:
        x = sp.Symbol('x')
        y = sp.Function('y')(x)
        
        eq_parts = differential_eq_str.split('=')
        differential_eq = sp.Eq(y.diff(x), sp.sympify(eq_parts[1]))
        print(differential_eq)
        solution = sp.dsolve(differential_eq)
        print(solution)
        y_expr = solution.args[1].args[1]  # Extract the right-hand side expression
        C1 = sp.Symbol('C1')
        y_eqn = y_expr + C1  # Remove the Eq() wrapper and use 'y_expr + C1' directly
        
        return solution
    except Exception as e:
        return f"Error: {e}"

def main():
    st.title("Differential Equation Solver")
    st.write("Enter a differential equation in the form 'dy/dx = ...' and click the 'Solve' button to see the solution.")

    differential_eq_str = st.text_area("Enter your differential equation:", height=100)

    if st.button("Solve"):
        if differential_eq_str:
            solution = solve_differential_eq(differential_eq_str)
            st.write("Solution:")
            latex_str = format_latex(solution)  # Format the solution in LaTeX
            st.latex(latex_str)  # Display the solution in the format "y = ..."
        else:
            st.warning("Please enter a valid differential equation.")

if __name__ == "__main__":
    main()
