#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bottle
import os
import psycopg2
import urllib

from bottle import *
from urllib import parse, request

parse.uses_netloc.append("postgres")
url = parse.urlparse(os.environ["DATABASE_URL"])

@route('/create')
def create_picnic():
    db = psycopg2.connect('picnic.db')
    db.execute("CREATE TABLE picnic (id INTEGER PRIMARY KEY, item CHAR(100) NOT NULL, quant INTEGER NOT NULL)")
    db.execute("INSERT INTO picnic (item,quant) VALUES ('bread', 4)")
    db.execute("INSERT INTO picnic (item,quant) VALUES ('cheese', 2)")
    db.execute("INSERT INTO picnic (item,quant) VALUES ('grapes', 30)")
    db.execute("INSERT INTO picnic (item,quant) VALUES ('cake', 1)")
    db.execute("INSERT INTO picnic (item,quant) VALUES ('soda', 4)")
    db.commit()


@route('/picnic')
def show_picnic():
    db = psycopg2.connect('picnic.db')
    c = db.cursor()
    c.execute("SELECT item,quant FROM picnic")
    data = c.fetchall()
    c.close()
    output = template('bring_to_picnic', rows=data)
    return output
    
run(host='0.0.0.0', port=argv[1])
