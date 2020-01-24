from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup
import sqlite3
import urllib.error
import ssl
from urllib.parse import urljoin


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('spider.sqlite')
spidercursor = conn.cursor()

spidercursor.execute('''CREATE TABLE IF NOT EXISTS Pages (id INTEGER PRIMARY KEY, url TEXT UNIQUE, html 
            TEXT, error INTEGER, old_rank REAL, new_rank REAL)''')
spidercursor.execute('''CREATE TABLE IF NOT EXISTS Links (from_id INTEGER, to_id INTEGER)''')
spidercursor.execute('''CREATE TABLE IF NOT EXISTS Webs (url TEXT UNIQUE)''')
spidercursor.execute('SELECT id,url FROM Pages WHERE html is NULL and error is NULL ORDER BY RANDOM() LIMIT 1')
row = spidercursor.fetchone()

if row is not None:
    print("Crawl is already been started!!!")
else:
    url = input('Enter web url or enter: ')
    if len(url) < 1  : url = 'http://www.dr-chuck.com/'
    if url.endswith('/')  : starturl = url[:-1]

    web = url

    if 'htm' in url:
        pos = url.rfind('/')
        web = url[:pos]

    if len(web) > 1:
        spidercursor.execute('INSERT OR IGNORE INTO Webs (url) VALUES ( ? )', (web,))
        spidercursor.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES ( ?, NULL, 1.0 )', (url,))
        conn.commit()


spidercursor.execute('''SELECT url FROM Webs''')
webs = list()
for row in spidercursor:
    webs.append(str(row[0]))

print(webs)

many = 0
while True:
    if many < 1:
        sval = input('How many pages:')
        if len(sval) < 1:break
        try:
            many = int(sval)
        except:
            print('Please enter a number')
            continue

    many = many - 1
    spidercursor.execute('SELECT id,url FROM Pages WHERE html is NULL and error is NULL ORDER BY RANDOM() LIMIT 1')

    try:
        row = spidercursor.fetchone()
        fromid = row[0]
        url = row[1]
    except:
        print('No HTML pages found which has not been retrieved')
        many = 0
        break

    print(fromid, url, end=' ')

    spidercursor.execute('DELETE from Links WHERE from_id=?', (fromid, ) )

    try:
        document = urlopen(url, context=ctx)
        html = document.read()

        if document.getcode() != 200 :
            print("Error: ",document.getcode())
            spidercursor.execute('UPDATE Pages SET error=? WHERE url=?', (document.getcode(), url))

        if 'text/html' != document.info().get_content_type() :
            print("Ignore non html page")
            spidercursor.execute('DELETE FROM Pages WHERE url=?', ( url, ) )
            conn.commit()
            continue

        print('('+str(len(html))+')', end=' ')
        soup = BeautifulSoup(html, "html.parser")

    except KeyboardInterrupt:
        print('')
        print('Program closed by user...')
        break

    except:
        print("Unable to retrieve or parse page")
        spidercursor.execute('UPDATE Pages SET error=-1 WHERE url=?', (url,))
        conn.commit()
        continue

    spidercursor.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES ( ?, NULL, 1.0 )', (url,))
    spidercursor.execute('UPDATE Pages SET html=? WHERE url=?', (memoryview(html), url))
    conn.commit()

    tags = soup('a')
    count = 0
    for tag in tags:
        href = tag.get('href', None)
        if href is None: continue
        up = urlparse(href)
        if len(up.scheme) < 1:
            href = urljoin(url, href)
        ipos = href.find('#')
        if ipos > 1: href = href[:ipos]
        if href.endswith('.png') or href.endswith('.jpg') or href.endswith('.gif'): continue
        if href.endswith('/'): href = href[:-1]

        if len(href) < 1: continue

        found = False
        for web in webs:
            if href.startswith(web):
                found = True
                break
        if not found:continue

        spidercursor.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES ( ?, NULL, 1.0 )', ( href,))
        count = count + 1
        conn.commit()
        spidercursor.execute('SELECT id FROM Pages WHERE url=? LIMIT 1', ( href, ))
        try:
            row = spidercursor.fetchone()
            toid = row[0]
        except:
            print('Could not retrieve id')
            continue
        spidercursor.execute('INSERT OR IGNORE INTO Links (from_id, to_id) VALUES ( ?, ? )', ( fromid, toid ) )


    print(count)

spidercursor.close()