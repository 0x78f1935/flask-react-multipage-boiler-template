from flask_classful import FlaskView, route
from flask import render_template

class IndexView(FlaskView):
    @route('/', methods=['GET'])
    def index(self):
        return render_template('views/index.jinja2')

    @route('/about', methods=['GET'])
    def about(self):
        return render_template('views/about.jinja2')
