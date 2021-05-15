#!/usr/bin/env python3
import logging
import subprocess as sp
from flask import Flask, request, send_file

PORT=38093

try:
    from config import *
except:
    pass

logging.basicConfig(level='INFO')
logger = logging.getLogger('gbs')

app = Flask(__name__)

@app.route('/gbs/', methods=['GET'])
def optimize ():
    since = request.args.get('since')
    recipient = request.args.get('recipient')
    script = """
    cd %s;
    git pull;
    git bundle create ../bundle %s..master;
    cd ..;
    rm bundle.enc;
    gpg --output bundle.enc --encrypt --recipient %s bundle
    """ % (PROJECT, since, recipient)
    sp.call(script, shell=True)
    return send_file('bundle.enc')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT, debug=True)
    pass


