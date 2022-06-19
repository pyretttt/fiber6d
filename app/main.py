"""
    Main app entry point.
"""

from flask import Flask, render_template

from blueprints import feed
from app.launcher import AppLauncher, Configuration

def home_view():
    return render_template('home.html', greetings='home page')

def create_app():
    global home_view
    app = Flask(__name__)
    
    # View registries
    app.register_blueprint(feed)
    home_view = app.route('/vlone')(home_view)

    return app

if __name__ == '__main__':
    config = Configuration.from_environment()
    launcher = AppLauncher(config)
    launcher.launch(create_app())