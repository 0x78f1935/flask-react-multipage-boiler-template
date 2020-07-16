## installation 

    python -m pip install virtualenv
    python -m virtualenv venv

activate virtuale environment

    .\venv\Scripts\activate

install requirements

    python -m pip install -r requirements.txt
    npm install

compile frontend

    npm run build

use hot-reload compile (for development purpose)

    npm run watch

start python server

    set FLASK_APP=webserver.py
    flask run

You can also use the provided visual studio code debug configuration. Just make sure to select the virtualenvironemnt in your IDE

open a browser and navigate to

    http://127.0.0.1:5000/

All set!