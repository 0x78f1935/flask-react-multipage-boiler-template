from flask_classful import FlaskView, route
from flask import render_template

class BoilerView(FlaskView):
    @route('/', methods=['GET'])
    def homepage(self):
        return render_template('views/homepage.jinja2')

    @route('/about', methods=['GET'])
    def about(self):
        return render_template('views/about.jinja2')

    @route('/marbles', methods=['GET'])
    def marble_game(self):
        return render_template('views/marbles.jinja2')