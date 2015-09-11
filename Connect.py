import sys
import psycopg2
import psycopg2.extras
import psycopg2.extensions

DATABASE_HOST = ''
DATABASE_NAME = ""  # Database login information not pushed to GitHub
USER_NAME = ''
PASSWORD = ''
SHOW_WHITE_SPACE = True # set to False if you need to trim column data

sql = """copy_from edited_subscribers TO '/tmp/subscribers123.csv' DELIMITER ',' CSV HEADER"""  # Was originally \copy but character was not escaped. Copy_into possibly




sys.stderr.write('Connecting to %s...\n' % DATABASE_HOST)
con = psycopg2.connect(database=DATABASE_NAME, user=USER_NAME, host=DATABASE_HOST, password=PASSWORD)

cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
sys.stderr.write("Executing: '%s'\n" % sql)
cur.execute(sql)

cur.close()
con.close()

