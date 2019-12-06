from cassandra.cluster import Cluster

cluster = Cluster()

session = cluster.connect('ks_teste')

session.execute("DELETE FROM ks_teste.agenda WHERE codigo IN (1,2)")

session.execute("INSERT INTO ks_teste.agenda(codigo,nome,telefone) VALUES (1, 'Charles', '999990000');")
session.execute("INSERT INTO ks_teste.agenda(codigo,nome,telefone) VALUES (2, 'Adriel', '11112222');")
session.execute("INSERT INTO ks_teste.agenda(codigo,nome,telefone) VALUES (3, 'Bob', '33334444');")

rows = session.execute("SELECT * FROM agenda;")

for row in rows:
    print (row.nome, row.telefone)

print("Fim")