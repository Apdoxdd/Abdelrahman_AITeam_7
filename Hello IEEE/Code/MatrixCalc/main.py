import FreeSimpleGUI as sg
import matrix as mat  # Assuming your functions are here

def create_matrix_input(rows, cols, prefix):
    """Generates a grid of input boxes for a matrix"""
    return [[sg.Input(size=(5, 1), key=f"-{prefix}_{r}_{c}-") for c in range(cols)] for r in range(rows)]

def get_matrix_values(values, rows, cols, prefix):
    """Retrieves data from the GUI grid and converts to a 2D list"""
    matrix = []			
    for r in range(rows):
        row = []
        for c in range(cols):
            val = values[f"-{prefix}_{r}_{c}-"]
            row.append(float(val) if val else 0.0)
        matrix.append(row)
    return matrix

def main():
    sg.theme('DarkGrey12')

    # --- Step 1: Select Operation ---
    ops = ["Matrix Sum", "Matrix Sub", "Matrix Mul", "Scalar Sum", "Scalar Sub", "Scalar Mul", "Normalize"]
    layout_start = [														
        [sg.Text("Select Matrix Operation:")],
        [sg.Combo(ops, key="OP", readonly=True, default_value=ops[0])],
        [sg.Button("Next")]
    ]

    window = sg.Window("Matrix Calculator", layout_start)
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        window.close()
        return

    operation = values["OP"]
    window.close()

    # --- Step 2: Define Dimensions ---
    # Determine if we need one or two matrices
    is_scalar = "Scalar" in operation
    is_norm = "Normalize" in operation
    
    dim_layout = [
        [sg.Text(f"Configure Dimensions for {operation}")],
        [sg.Text("Matrix A: Rows"), sg.Input("2", size=(3,1), key="-R1-"), sg.Text("Cols"), sg.Input("2", size=(3,1), key="-C1-")]
    ]
    # // only show a first in case different opeation can even add timer prob
    if not is_scalar and not is_norm:
        dim_layout.append([sg.Text("Matrix B: Rows"), sg.Input("2", size=(3,1), key="-R2-"), sg.Text("Cols"), sg.Input("2", size=(3,1), key="-C2-")])
    elif is_scalar:
        dim_layout.append([sg.Text("Scalar Value:"), sg.Input("1", size=(5,1), key="-SCALAR-")])

    dim_layout.append([sg.Button("Generate Grid")])
    
    window = sg.Window("Dimensions", dim_layout)
    event, values = window.read()
    
    r1, c1 = int(values["-R1-"]), int(values["-C1-"])
    r2, c2 = (int(values.get("-R2-", 0)), int(values.get("-C2-", 0))) #incase we chose scalar lol
    scalar = float(values.get("-SCALAR-", 0))
    window.close()

    grid_layout = [[sg.Text(f"Enter values for {operation}:")]]
    grid_layout.append([sg.Text("Matrix A")])
    grid_layout.extend(create_matrix_input(r1, c1, "A"))

    if not is_scalar and not is_norm:
        grid_layout.append([sg.Text("Matrix B")])
        grid_layout.extend(create_matrix_input(r2, c2, "B"))

    grid_layout.append([sg.Button("Calculate")])
    
    window = sg.Window("Data Entry", grid_layout)
    event, values = window.read()

    if event == "Calculate":
        matrix_a = get_matrix_values(values, r1, c1, "A")
        result = None

        if operation == "Matrix Sum":
            matrix_b = get_matrix_values(values, r2, c2, "B")
            result = mat.matsum(matrix_a, matrix_b)
        elif operation == "Matrix Sub":
            matrix_b = get_matrix_values(values, r2, c2, "B")
            result = mat.matsub(matrix_a, matrix_b)
        elif operation == "Matrix Mul":
            matrix_b = get_matrix_values(values, r2, c2, "B")
            result = mat.matmul(matrix_a, matrix_b)
        elif operation == "Scalar Sum":
            result = mat.scalarsum(scalar, matrix_a)
        elif operation == "Scalar Sub":
            result = mat.scalarsub(scalar, matrix_a)
        elif operation == "Scalar Mul":
            result = mat.scalarmul(scalar, matrix_a)
        elif operation == "Normalize":
            result = mat.matnorm(matrix_a)
	
        if result:
            res_str = "\n".join(["\t".join([f"{val:.2f}" for val in row]) for row in result])
            sg.popup_scrolled("Resulting Matrix:", res_str, font="Courier 12")
        else:
            sg.popup_error("Error in calculation. Check dimensions!")

    window.close()

if __name__ == "__main__":
    main()		