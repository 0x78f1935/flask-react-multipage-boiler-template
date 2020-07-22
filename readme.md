[![Build Status](https://img.shields.io/github/forks/0x78f1935/flask-react-multipage-boiler-template.svg?style=for-the-badge)](https://github.com/0x78f1935/flask-react-multipage-boiler-template)
[![Build Status](https://img.shields.io/github/stars/0x78f1935/flask-react-multipage-boiler-template.svg?style=for-the-badge)](https://github.com/0x78f1935/flask-react-multipage-boiler-template)
[![License](https://img.shields.io/github/license/0x78f1935/flask-react-multipage-boiler-template.svg?style=for-the-badge)](https://github.com/0x78f1935/flask-react-multipage-boiler-template)
[![Build Status](https://img.shields.io/travis/0x78f1935/flask-react-multipage-boiler-template/master.svg?style=for-the-badge)](https://travis-ci.org/0x78f1935/flask-react-multipage-boiler-template)
[![Dependency Status](https://img.shields.io/david/0x78f1935/flask-react-multipage-boiler-template.svg?style=for-the-badge)](https://david-dm.org/0x78f1935/flask-react-multipage-boiler-template)
[![peerDependency Status](https://img.shields.io/david/peer/0x78f1935/flask-react-multipage-boiler-template.svg?style=for-the-badge)](https://david-dm.org/0x78f1935/flask-react-multipage-boiler-template#info=devDependencies)

## pre development steps

In order to keep your configuration file safe. After cloning the repository execute the following command

    git update-index --assume-unchanged backend/config/__init__.py

## installation Python 3.6 >

    python -m pip install virtualenv
    python -m virtualenv venv

activate virtuale environment windows

    .\venv\Scripts\activate

activate virtuale environment debian

    source venv/bin/activate

install requirements

    python -m pip install -r requirements.txt
    npm install

compile frontend

    npm run build

use hot-reload compile (for development purpose)

    npm run watch

start python server windows

    set FLASK_APP=webserver.py
    flask run

start python server debian

    export FLASK_APP=webserver.py
    flask run

You can also use the provided visual studio code debug configuration. Just make sure to select the virtualenvironemnt in your IDE

open a browser and navigate to

    http://127.0.0.1:5000/

All set!