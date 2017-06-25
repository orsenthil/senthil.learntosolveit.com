from tabulate import tabulate

table_header = ["graph", "vertex", "edge"]

items = [
    ["communication", "telephone, computer", "fiber optic cable"],
    ["circuit", "gate, register, processor", "wire"],
    ["mechanical", "joint", "rod, beam, spring"],
    ["financial", "stock, currency", "transactions"],
    ["transportation", "street intersection, airport", "highway, airway route"],
    ["internet", "class C network", "connection"],
    ["game", "board position", "legal move"],
    ["social relationship", "person, actor", "friendship, movie cast"],
    ["neural network", "neuron", "synapse"],
    ["protein network", "protein", "protein-protein interaction"],
    ["molecule", "atom", "bond"]]

print(tabulate(items, headers=table_header, tablefmt="rst"))
