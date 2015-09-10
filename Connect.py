import sys
import psycopg2
import psycopg2.extras
import psycopg2.extensions

DATABASE_HOST = 'ec2-54-204-20-209.compute-1.amazonaws.com'
DATABASE_NAME = "d5qsnqpppo4nkq"
SCHEMA = 'postgres'
USER_NAME = 'edbiaisfnankjt'
PASSWORD = ' _9F3AzzV1QSm9tEVu3tlrcoGcI'
SHOW_WHITE_SPACE = True # set to False if you need to trim column data

sql = """\copy edited_subscribers TO '/tmp/subscribers.csv' DELIMITER ',' CSV HEADER"""

sql = """SELECT * FROM subscribers WHERE edited=True AND flagged=False"""  # I want to combine both queries
