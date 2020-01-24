import sqlite3

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()
print("Creating JSON output on spider.js...")
many = int(input("How many nodes? "))

cur.execute('''SELECT COUNT(from_id) AS inbound, old_rank, new_rank, id, url 
    FROM Pages JOIN Links ON Pages.id = Links.to_id
    WHERE html IS NOT NULL AND ERROR IS NULL
    GROUP BY id ORDER BY id,inbound''')

filehandle = open('spider.js','w')

nodes = list()
maxrank = None
minrank = None

for row in cur :
    nodes.append(row)
    rank = row[2]
    if maxrank is None or maxrank < rank: maxrank = rank
    if minrank is None or minrank > rank : minrank = rank
    if len(nodes) > many : break

if maxrank == minrank or maxrank is None or minrank is None:
    print("Error - please run rank computation to compute page rank")
    quit()

filehandle.write('spiderJson = {"nodes":[\n')
count = 0
map = dict()
ranks = dict()


for row in nodes :
    if count > 0 : filehandle.write(',\n')
    rank = row[2]
    rank = 19 * ( (rank - minrank) / (maxrank - minrank) ) #calculating weignt
    filehandle.write('{'+'"weight":'+str(row[0])+',"rank":'+str(rank)+',')
    filehandle.write(' "id":'+str(row[3])+', "url":"'+row[4]+'"}')
    map[row[3]] = count
    ranks[row[3]] = rank
    count = count + 1


filehandle.write('],\n')
filehandle.write('"links":[\n')

cur.execute('''SELECT DISTINCT from_id, to_id FROM Links''')
count = 0
for row in cur :
    # print row
    if row[0] not in map or row[1] not in map : continue
    if count > 0 : filehandle.write(',\n')
    rank = ranks[row[0]]
    srank = 19 * ( (rank - minrank) / (maxrank - minrank) )
    filehandle.write('{"source":'+str(map[row[0]])+',"target":'+str(map[row[1]])+',"value":3}')
    count = count + 1


filehandle.write(']};')
filehandle.close()
cur.close()
