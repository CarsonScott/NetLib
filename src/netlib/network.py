from .util import Template, Object
import pickle

class Network:

	def __init__(self, node=Template(), link=Template(), undirected=False):
		self.node_template = Template(**node)
		self.link_template = Template(**link)
		self.nodes = []
		self.links = []
		self.pairs = []
		self.sources = []
		self.targets = []
		self.iteration = -1
		self.undirected = undirected

	def create_node(self, *args, **kwargs):
		if len(args) != 1 or not isinstance(args[0], Object):
			node = self.node_template(*args, **kwargs)
		else: node = args[0]
		self.nodes.append(node)
		self.sources.append([])
		self.targets.append([])
		index = len(self.nodes) - 1
		return index

	def create_link(self, source, target, *args, **kwargs):
		if not self.link_exists(source, target):
			if len(args) != 1 or not isinstance(args[0], Object):
				link = self.link_template(*args, **kwargs)
			else: link = args[0]
			self.links.append(link)
			self.pairs.append((source, target))
			self.sources[target].append(source)
			self.targets[source].append(target)
			index = len(self.links) - 1
			return index
		else: raise Exception('Link already exists: ' + str((source, target)))	

	def remove_link(self, source, target):
		if self.link_exists(source, target):
			if self.undirected and (source, target) not in self.pairs:
				source, target = target, source
			index = self.pairs.index((source, target))
			self.sources[target].remove(source)
			self.targets[source].remove(target)
			del self.pairs[index]
			del self.links[index]
		else: raise Exception('Link does not exist: ' + str(pair))

	def get_node(self, index):
		return self.nodes[index]

	def get_link(self, source, target):
		if self.link_exists(source, target):
			if self.undirected and (source, target) not in self.pairs:
				source, target = target, source
			index = self.pairs.index((source, target))
			return self.links[index]

	def get_sources(self, index):
		if self.undirected:
			return self.sources[index] + self.targets[index]
		else: return self.sources[index]

	def get_targets(self, index):
		if self.undirected:
			return self.targets[index] + self.sources[index]
		else: return self.targets[index]

	def node_exists(self, index):
		return index < len(self.nodes) - 1

	def link_exists(self, source, target):
		return (source, target) in self.pairs or self.undirected and (target, source) in self.pairs

	def load(self, filename):
		return pickle.load(open(filename, 'rb'))

	def dump(self, filename):
		pickle.dump(self, open(filename, 'wb'))

	def update(self):
		self.iteration += 1
		for i in range(len(self.nodes)):
			self.refresh(i)
		for i in range(len(self.nodes)):
			self.compute(i)

	def refresh(self, i):
		pass

	def compute(self, i):
		pass

