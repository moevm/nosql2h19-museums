from py2neo import Graph

g=Graph()
g.run("match (n) detach delete n")
g.run("CREATE (n:Person {name:{name}}) RETURN n", name="Teacher")

for i in range(7):
   g.run("CREATE (n:Person {name:{name}}) RETURN n", name="Student_"+str(i+1))
for i in range(7):
   g.run("MATCH (a:Person),(b:Person) WHERE a.name = {namef} AND b.name = {namel} CREATE (a)-[r:FRIENDS_WITH{name: a.name + '<-->' + b.name}]->(b)", namef="Student_"+str(i+1), namel="Student_"+str(random.randint(1,7)))
for i in range(7):
   g.run("MATCH (a:Person),(b:Person) WHERE a.name = {namef} AND b.name = {namel} CREATE (a)-[r:HATES{name: a.name + '<!!>' + b.name}]->(b)", namef="Student_"+str(i+1), namel="Student_"+str(random.randint(1,7)))
