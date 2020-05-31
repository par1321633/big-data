import logging
from logging.handlers import RotatingFileHandler

from flask import Flask

log_files = {
    'info' : 'log\info.log',
    'error' : 'log\error.log',
    'warning' : 'log\warning.log'
}

app = Flask(__name__)

@app.route('/')
def foo():
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    app.logger.info('Info')
    return "foo"

def set_loggers(app):
    handler = RotatingFileHandler(log_files['info'], maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(handler)

    handler = RotatingFileHandler(log_files['error'], maxBytes=10000, backupCount=1)
    handler.setLevel(logging.ERROR)
    app.logger.setLevel(logging.ERROR)
    app.logger.addHandler(handler)

    handler = RotatingFileHandler(log_files['warning'], maxBytes=10000, backupCount=1)
    handler.setLevel(logging.WARNING)
    app.logger.setLevel(logging.WARNING)
    app.logger.addHandler(handler)

if __name__ == '__main__':
    set_loggers(app)
    app.run()