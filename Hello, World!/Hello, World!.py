from py2neo import Graph

graph=Graph()

for name in ["Hello","World","!"]:
    graph.run("CREATE (n:Person {name:{name}}) RETURN n", name=name)
