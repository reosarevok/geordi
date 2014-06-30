from werkzeug.serving import run_simple
from geordi import create_app

application = create_app()

if __name__ == "__main__":
    run_simple('0.0.0.0', 5000, application, use_reloader=True, use_debugger=True)
