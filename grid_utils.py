#!/usr/bin/env python 

class Node(object):

	def __init__(self, name):
		self.name = name
		self.nodes = list()

	def add(self, node, weight=1):
		self.nodes.append(node)

	def print_nodes(self, lines='|_______', path=[]):
		for node in self.nodes:
			print('{}{}'.format(lines, node.name))
			if node.name not in path:
				path.append(node.name)
				node.print_nodes('\t' + lines, path)

class Graph(object):

	def __init__(self, start_nodes):
		self.start_nodes = start_nodes

	def print_graph(self):
		for node in self.start_nodes:
			print(node.name)
			node.print_nodes()

	def find_path(self, name, node, path=[], paths=[]):
		path = path + [node.name]
		if node.name == name:
			return path
		for node in node.nodes:
			if node.name not in path:
				newpath = self.find_path(name, node, path, paths)
				if newpath is not None:
					paths.append(newpath)
		return None

	def find_shortest_path(self, name, node):
		paths = []
		self.find_path(name, node, [], paths)
		if not paths:
			return None
		min_path = paths[0]
		for path in paths:
			if len(path) > len(min_path):
				min_path = path
		return path


if __name__ == "__main__":
	a = Node('A')
	b = Node('B')
	c = Node('C')
	d = Node('D')
	e = Node('E')
	f = Node('F')
	g = Node('G')

	a.add(b)
	a.add(c)
	b.add(c)
	b.add(d)
	c.add(d)
	d.add(c)
	e.add(f)
	f.add(c)

	start_nodes = [a, e]
	graph = Graph(start_nodes)
	graph.print_graph()
	paths = []
	graph.find_path('D', a, [], paths)
	print(paths)

	print(graph.find_shortest_path('D', a))


