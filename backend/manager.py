#! /usr/bin/env python
import sys
import types
import os
import pathlib

# pylint: disable=import-outside-toplevel
description = \
    '''
    CLI for doing different tasks with the Flask object.
    Public methods exposed in this file cannot take any input parameters.

    Usage: ./manager.py <function-name>
        where <function-name> corresponds to a method defined in this file, and
        accepts no parameters.
    '''

CURR_FILE_DIR = pathlib.Path(__file__).parent.absolute()

def run():
    '''
    Runs the app in debug mode for local development.
    '''
    if not os.environ.get('APP_CONFIG', None):
        os.environ.update({'APP_CONFIG': os.path.join(CURR_FILE_DIR, 'config.py')})
    from server import app
    app.run('0.0.0.0', 8000, debug=True)


def init_tables():
    '''
    Initializes all the tables in db at SQL_CONNECTION_URI.
    '''
    from glob import glob
    import importlib
    from sqlalchemy import create_engine
    from config import SQLALCHEMY_DATABASE_URI
    from server.models import Base
    # Import all model objects dynamically so Base...create_all() works
    model_base = 'server.models.'
    model_files = glob(os.path.join(CURR_FILE_DIR, './server/models/*.py'))
    model_names = list(filter(
        lambda fn: not fn.startswith('__'),
        map(lambda fn: os.path.basename(fn)[:-3], model_files)
    ))
    for name in model_names:
        package_name = model_base + name
        print('Importing model package: {}'.format(package_name))
        importlib.import_module(package_name)
    db_engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
    Base.metadata.create_all(db_engine)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(description)
        sys.exit(1)
    action = sys.argv[1]
    _locals = locals()
    local_functions = list(filter(
        lambda loc: isinstance(_locals[loc], types.FunctionType), _locals))
    if action not in local_functions:
        print(description)
        sys.exit(1)

    _locals[action]()
