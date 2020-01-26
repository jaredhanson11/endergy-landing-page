'''
Runs development version of the server application.
'''

import os
import pathlib


if __name__ == '__main__':
    if not os.environ.get('APP_CONFIG', None):
        # pylint: disable=invalid-name
        curr_path = pathlib.Path(__file__).parent.absolute()
        # pylint: enable=invalid-name
        os.environ.update({'APP_CONFIG': os.path.join(curr_path, 'config.py')})
    from server import app
    app.run('0.0.0.0', 8000, debug=True)
