## Note: This is covalent compounds only
elements = {
    "H":  {"name": "Hydrogen",  "atomicNumber": 1,  "atomicMass": 1.008,  "valenceElectrons": 1, "maxElectrons": 2},
    "He": {"name": "Helium",    "atomicNumber": 2,  "atomicMass": 4.0026, "valenceElectrons": 2, "maxElectrons": 2},
    "Li": {"name": "Lithium",   "atomicNumber": 3,  "atomicMass": 6.94,   "valenceElectrons": 1, "maxElectrons": 8},
    "Be": {"name": "Beryllium", "atomicNumber": 4,  "atomicMass": 9.0122, "valenceElectrons": 2, "maxElectrons": 8},
    "B":  {"name": "Boron",     "atomicNumber": 5,  "atomicMass": 10.81,  "valenceElectrons": 3, "maxElectrons": 8},
    "C":  {"name": "Carbon",    "atomicNumber": 6,  "atomicMass": 12.011, "valenceElectrons": 4, "maxElectrons": 8},
    "N":  {"name": "Nitrogen",  "atomicNumber": 7,  "atomicMass": 14.007, "valenceElectrons": 5, "maxElectrons": 8},
    "O":  {"name": "Oxygen",    "atomicNumber": 8,  "atomicMass": 15.999, "valenceElectrons": 6, "maxElectrons": 8},
    "F":  {"name": "Fluorine",  "atomicNumber": 9,  "atomicMass": 18.998, "valenceElectrons": 7, "maxElectrons": 8},
    "Ne": {"name": "Neon",      "atomicNumber": 10, "atomicMass": 20.180, "valenceElectrons": 8, "maxElectrons": 8},
    "Na": {"name": "Sodium",    "atomicNumber": 11, "atomicMass": 22.990, "valenceElectrons": 1, "maxElectrons": 8},
    "Mg": {"name": "Magnesium", "atomicNumber": 12, "atomicMass": 24.305, "valenceElectrons": 2, "maxElectrons": 8},
    "Al": {"name": "Aluminum",  "atomicNumber": 13, "atomicMass": 26.982, "valenceElectrons": 3, "maxElectrons": 8},
    "Si": {"name": "Silicon",   "atomicNumber": 14, "atomicMass": 28.085, "valenceElectrons": 4, "maxElectrons": 8},
    "P":  {"name": "Phosphorus","atomicNumber": 15, "atomicMass": 30.974, "valenceElectrons": 5, "maxElectrons": 8},
    "S":  {"name": "Sulfur",    "atomicNumber": 16, "atomicMass": 32.06,  "valenceElectrons": 6, "maxElectrons": 8},
    "Cl": {"name": "Chlorine",  "atomicNumber": 17, "atomicMass": 35.45,  "valenceElectrons": 7, "maxElectrons": 8},
    "Ar": {"name": "Argon",     "atomicNumber": 18, "atomicMass": 39.948, "valenceElectrons": 8, "maxElectrons": 8},
    "K":  {"name": "Potassium", "atomicNumber": 19, "atomicMass": 39.098, "valenceElectrons": 1, "maxElectrons": 8},
    "Ca": {"name": "Calcium",   "atomicNumber": 20, "atomicMass": 40.078, "valenceElectrons": 2, "maxElectrons": 8}
}

class Atom:
    def __init__(self, element):
        self.name = elements[element]["name"]
        self.symbol = element
        self.valence = elements[element]["valenceElectrons"]
        self.maxElectrons = elements[element]["maxElectrons"]

    def canBond(self):
        return self.valence < self.maxElectrons

    def electrons_needed(self):
        return self.maxElectrons - self.valence

    def __repr__(self):
        return f"{self.symbol} ({self.valence}/{self.maxElectrons})"


def bond(atom1, atom2):
    while atom1.canBond() and atom2.canBond():
        atom1.valence += 1
        atom2.valence += 1
        moleculeName = atom1.symbol+atom2.symbol;

        if(atom1.symbol == atom2.symbol):
            moleculeName = atom1.symbol+"₂"
        
        if not atom1.canBond() and not atom2.canBond():
            print(f"{atom1} and {atom2} have bonded to form {moleculeName}")
            break;
        else:
            if atom1.canBond() and atom2.canBond():
                print(f"Bond is in progress..."); 
            elif atom1.canBond() and not atom2.canBond():
                print(f"{atom1} and {atom2} bonded but {atom1} still need electrons. We might need another {atom2.name} atom");
                break;
            elif atom2.canBond() and not atom1.canBond():
                print(f"{atom1} and {atom2} bonded but {atom2} still need electrons. We might need another {atom1.name} atom")    
                break;
    else:
        print(f"{atom1} and {atom2} cannot bond")

bond(Atom("S"), Atom("Cl"))
