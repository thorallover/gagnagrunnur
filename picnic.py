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
