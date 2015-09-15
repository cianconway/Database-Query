import sys
import psycopg2
import psycopg2.extras
import psycopg2.extensions

DATABASE_HOST = 'ec2-54-204-20-209.compute-1.amazonaws.com'
DATABASE_NAME = "d5qsnqpppo4nkq"
USER_NAME = 'edbiaisfnankjt'
PASSWORD = '_9F3AzzV1QSm9tEVu3tlrcoGcI'
SHOW_WHITE_SPACE = True # set to False if you need to trim column data

sql = """SELECT * FROM edited_subscribers WHERE edited=True AND flagged=False"""




sys.stderr.write('Connecting to %s...\n' % DATABASE_HOST)
con = psycopg2.connect(database=DATABASE_NAME, user=USER_NAME, host=DATABASE_HOST, password=PASSWORD)

cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
sys.stderr.write("Executing: '%s'\n" % sql)
cur.execute(sql)

cur.close()
con.close()

