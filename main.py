file = input("Enter the PDB file name: ")
processed_file = file.split(".")[0] + "_processed.pdb"

with open(file, "r") as f:
    for line in f:
        if line.startswith("HETATM") or line.startswith("CONECT"):
            pass
        else:
            data = line.strip()+"\n"
        with open(processed_file, "a") as f:
            f.write(data)
