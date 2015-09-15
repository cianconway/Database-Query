import sys
import psycopg2
import psycopg2.extras
import psycopg2.extensions

DATABASE_HOST = ''
DATABASE_NAME = ""
USER_NAME = ''
PASSWORD = ''
SHOW_WHITE_SPACE = True # set to False if you need to trim column data

sql = """\copy (SELECT * FROM edited_subscribers WHERE edited=True AND flagged=False) TO '/tmp/subscribers.csv' DELIMITER ',' CSV HEADER"""





sys.stderr.write('Connecting to %s...\n' % DATABASE_HOST)
con = psycopg2.connect(database=DATABASE_NAME, user=USER_NAME, host=DATABASE_HOST, password=PASSWORD)

cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
sys.stderr.write("Executing: '%s'\n" % sql)
cur.execute(sql)

cur.close()
con.close()

