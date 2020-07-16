from backend import Webserver, db

server = Webserver()._start()

def start_le_server():
    server = Webserver()._start()
    print("* Application started ...")
    return server

@server.shell_context_processor
def make_shell_context():
    return {
        'app': server,
        'db': db
    }
