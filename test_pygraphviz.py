import pygraphviz as pgv

A = pgv.AGraph()
A.add_edge('A', 'B')
A.layout(prog='dot')
A.draw('graph.png')
print("Graph created and saved as 'graph.png'.")