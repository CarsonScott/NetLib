# NetLib

NetLib is a lightweight python library that lets you define, construct, and operate on networks with ease.

### Templates

Templates are structures that represent "classes" defined at runtime, which can be instantiated to create objects. 

    T = Template('x', 'y')
    obj = T(1, 2)

    obj.x 
    >> 1

    obj.y
    >> 2

### Networks

A network contains a node template and a link template from which all nodes and links are created. This means that every node shares the same set of attributes, as does every link.

	node = Template('x', 'y')
	link = Template('w')

    network = Network(node, link)

Each node is assigned an index when created which allows it to be identified. Each link is created given a pair of indices representing the source and target nodes.

	i = network.create_node(x=1, y=2)
	j = network.create_node(x=3, y=4)

	network.create_link(i, j, w=0.5)

### Network Automata

A network automaton is a functional network that updates each of its nodes based only on the surrounding neighborhood. The network class has a function called compute that takes an index and updates the corresponding node. Network Automata are created by making a new class that inherits from Network and defining the compute function. 
