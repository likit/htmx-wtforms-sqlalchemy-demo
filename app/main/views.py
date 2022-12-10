from app.main import main_blueprint as main


@main.route('/')
def index():
    return 'Welcome to the online room booking service.'
