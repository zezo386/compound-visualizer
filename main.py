element_protons = {1:'Hydrogen', 2:'Helium', 3:'Lithium', 4:'Beryllium', 5:'Boron',6:'Carbon',7:'Nitrogen',8:'Oxygen',9:'Fluorine',10:'Neon',11:'Sodium',12:'Magnesium',13:'Aluminum',14:'Silicon',15:'Phosphorus',16:'Sulfur',17:'Chlorine',18:'Argon',19:'Potassium',20:'Calcium',21:'Scandium',22:'Titanium',23:'Vanadium',24:'Chromium',25:'Manganese',26:'Iron',27:'Cobalt',28:'Nickel',29:'Copper',30:'Zinc',31:'Gallium',32:'Germanium',33:'Arsenic',34:'Selenium',35:'Bromine',36:'Krypton',37:'Rubidium',38:'Strontium',39:'Yttrium',40:'Zirconium',41:'Niobium',42:'Molybdenum',43:'Technetium',44:'Ruthenium',45:'Rhodium',46:'Palladium',47:'Silver',48:'Cadmium',49:'Indium',50:'Tin',51:'Antimony',52:'Tellurium',53:'Iodine',54:'Xenon',55:'Cesium',56:'Barium',57:'Lanthanum',58:'Cerium',59:'Praseodymium',60:'Neodymium',61:'Promethium',62:'Samarium',63:'Europium',64:'Gadolinium',65:'Terbium',66:'Dysprosium',67:'Holmium',68:'Erbium',69:'Thulium',70:'Ytterbium',71:'Lutetium',72:'Hafnium',73:'Tantalum',74:'Tungsten',75:'Rhenium',76:'Osmium',77:'Iridium',78:'Platinum',79:'Gold',80:'Mercury',81:'Thallium',82:'Lead',83:'Bismuth',84:'Polonium',85:'Astatine',86:'Radon',87:'Francium',88:'Radium',89:'Actinium',90:'Thorium',91:'Protactinium',92:'Uranium',93:'Neptunium',94:'Plutonium',95:'Americium',96:'Curium',97:'Berkelium',98:'Californium',99:'Einsteinium',100:'Fermium',101:'Mendelevium',102:'Nobelium',103:'Lawrencium',104:'Rutherfordium',105:'Dubnium',106:'Seaborgium',107:"Bohrium",108:"Hassium",109:"Meitnerium",110:"Darmstadtium",111:"Roentgenium",112:"Copernicium",113:"Nihonium",114:"Flerovium",115:"Moscovium",116:"Livermorium",117:"Tennessine",118:"Oganesson"}
element_symbols = {1:"H",2:"He",3:"Li",4:"Be",5:"B",6:"C",7:"N",8:"O",9:"F",10:"Ne",11:"Na",12:"Mg",13:"Al",14:"Si",15:"P",16:"S",17:"Cl",18:"Ar",19:"K",20:"Ca",21:"Sc",22:"Ti",23:"V",24:"Cr",25:"Mn",26:"Fe",27:"Co",28:"Ni",29:"Cu",30:"Zn",31:"Ga",32:"Ge",33:"As",34:"Se",35:"Br",36:"Kr",37:"Rb",38:"Sr",39:"Y",40:"Zr",41:"Nb",42:"Mo",43:"Tc",44:"Ru",45:"Rh",46:"Pd",47:"Ag",48:"Cd",49:"In",50:"Sn",51:"Sb",52:"Te",53:"I",54:"Xe",55:"Cs",56:"Ba",57:"La",58:"Ce",59:"Pr",60:"Nd",61:"Pm",62:"Sm",63:"Eu",64:"Gd",65:"Tb",66:"Dy",67:"Ho",68:"Er",69:"Tm",70:"Yb",71:"Lu",72:"Hf",73:"Ta",74:"W",75:"Re",76:"Os",77:"Ir",78:"Pt",79:"Au",80:"Hg",81:"Tl",82:"Pb",83:"Bi",84:"Po",85:"At",86:"Rn",87:"Fr",88:"Ra",89:'Ac',90:'Th',91:'Pa',92:'U',93:'Np',94:'Pu',95:'Am',96:'Cm',97:'Bk',98:'Cf',99:'Es',100:'Fm',101:'Md',102:'No',103:'Lr',104:'Rf',105:'Db',106:'Sg',107:'Bh',108:'Hs',109:'Mt',110:'Ds',111:'Rg',112:'Cn',113:'Nh',114:'Fl',115:'Mc',116:'Lv',117:'Ts',118:'Og'}
def get_element_name(atomic_number):
    return element_protons.get(atomic_number, "Unknown Element")
def get_ion(atomic_number,charge):
    element_name = get_element_name(atomic_number)
    if element_name == "Unknown Element":
        return element_name
    if charge > 0:
        return f"{element_name} {charge}+"
    elif charge < 0:
        return f"{element_name} {abs(charge)}-"
    else:
        return element_name

class Atom:
    def __init__(self,atomic_number,mass_number,charge=0):
        self.number_of_protons = atomic_number
        self.number_of_neutrons = mass_number - atomic_number
        self.number_of_electrons = atomic_number - charge
        self.element_name = get_element_name(atomic_number)
        self.element_symbol = element_symbols.get(atomic_number, "X")
        self.charge = charge
        self.type = "Metal" if atomic_number in [3,4,11,12,19,20,37,38,55,56,87,88] else "Non-metal"
        self.valence = self.get_valence_electrons()
    def get_valence_electrons(self):
        shells = [2, 8, 18, 32, 50, 72, 98]
        remaining_electrons = self.number_of_electrons
        for shell_capacity in shells:
            if remaining_electrons > shell_capacity:
                valence = shell_capacity
                remaining_electrons -= shell_capacity
            else:
                valence = remaining_electrons
                break
        return valence
    def __repr__(self):
        ion_representation = get_ion(self.number_of_protons, self.charge)
        return f"{ion_representation}"


class Chemical_Bond:
    def __init__(self,atom1,atom2):
        self.atom1 = atom1
        self.atom2 = atom2
        self.bond_type = "Ionic bond" if (atom1.type == "Metal" and  atom2.type == "Non-metal") or (atom1.type == "Non-metal" and atom2.type == "Metal") else "Covalent bond" if atom1.type == "Non-metal" and atom2.type == "Non-metal" else "Metallic bond" if atom1.type == "Metal" and atom2.type == "Metal" else "Unknown bond"
    def __repr__(self):
        return f"{self.bond_type} bond between {self.atom1} and {self.atom2}"


class Chemical_compound:
    def __init__(self,bonds):
        self.bonds = bonds
        self.atoms = {}
        for i in bonds:
            if self.atoms.get(i.atom1) is None:
                self.atoms[i.atom1] = 0
            if self.atoms.get(i.atom2) is None:
                self.atoms[i.atom2] = 0
            self.atoms[i.atom1] += 1
            self.atoms[i.atom2] += 1
    def __repr__(self):
        atom_list = f"{'; '.join([f'{str(atom)}: {count}' for atom, count in self.atoms.items()])}"
        bond_list = '; '.join([str(bond) for bond in self.bonds])
        return f"Chemical Compound with Atoms: {atom_list} and Bonds: {bond_list}"
    def graphical_visualization(self):
        import matplotlib.pyplot as plt
        import networkx as nx

        G = nx.Graph()
        for bond in self.bonds:
            G.add_node(bond.atom1)
            G.add_node(bond.atom2)
            G.add_edge(bond.atom1, bond.atom2)

        pos = nx.spring_layout(G)

        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold')
        plt.title("Chemical Compound Visualization")
        plt.show()

atoms = []
while True:
    while True:
        try:
            atomic_number = int(input("Enter atomic number of the element (1-118): "))
            if 1 <= atomic_number <= 118:
                break
            else:
                print("Please enter a valid atomic number between 1 and 118.")
        except ValueError:
            print("Invalid input. Please enter an integer value.")
    while True:
        try:
            mass_number = int(input("Enter mass number of the element: "))
            if mass_number >= atomic_number:
                break
            else:
                print("Mass number must be greater than or equal to atomic number.")
        except ValueError:
            print("Invalid input. Please enter an integer value.")
    while True:
        try:
            charge = int(input("Enter charge of the element (default is 0): ") or "0")
            break
        except ValueError:
            print("Invalid input. Please enter an integer value.")
    atom = Atom(atomic_number,mass_number,charge)
    atoms.append(atom)
    print(f"Created Atom: {atom}")
    another = input("Do you want to create another atom? (y/n): ").lower()
    if another != 'y':
        break
bonds = []
for i in range(len(atoms)-1):
    bond = Chemical_Bond(atoms[i],atoms[i+1])
    bonds.append(bond)
compound = Chemical_compound(bonds)
visualize = input("Do you want to visualize the compound? (y/n): ").lower()
if visualize == 'y':
    compound.graphical_visualization()




        

