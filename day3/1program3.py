#Box Grid Printer

def print_box_grid(rows, cols):
    for i in range(rows):
        print("+" + "-" * 4 + "+" + "-" * 4 + "+")
        for j in range(4):
            print("/" + " " * 4 + "/" + " " * 4 + "/")
    print("+" + "-" * 4 + "+" + "-" * 4 + "+")
print_box_grid(2, 2)
