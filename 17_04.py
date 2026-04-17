import sys

def get_arg_invalid():
    print("Invalid arguments")
    return False, False, False
    

def get_arg(argv):
    try:
        poly1 = argv[argv.index("-i") + 1]
        poly2 = argv[argv.index("-i") + 2]
        if (poly2 == "-o" or poly1 == "-o"):
            get_arg_invalid()
        outputfile = argv[argv.index("-o") + 1]
        print(poly1, poly2, outputfile)
        return poly1, poly2, outputfile
    except Exception:
        get_arg_invalid()

def read_poly(filepath):
    with open(filepath, "r") as f:
        poly = []
        for line in f:
            line = line.strip()
            if line:
                poly.append(line.split(", "))
        return poly

def multiply_polys(poly1, poly2):
    multiplied_poly = []
    for term in poly1:
        for term2 in poly2:
            coeff = int(term[0]) * int(term2[0])
            power = int(term[1]) + int(term2[1])
            multiplied_poly.append([coeff, power])
    return multiplied_poly

if __name__ == '__main__':
    poly1, poly2, outputfile = get_arg(sys.argv)
    if not poly1 or not poly2 or not outputfile:
        print("Try again")
    else:
        with open(outputfile, "w") as f:
            for line in multiply_polys(read_poly(poly1), read_poly(poly2)):
                f.write(f"{line[0]}, {line[1]}\n")
            f.close()
