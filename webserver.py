from backend import Webserver, db
from backend._cli import register

server = Webserver()._start()
register(server)

def start_le_server():
    server = Webserver()._start()
    print("* Application started ...")
    register(server)
    return server

@server.shell_context_processor
def make_shell_context():
    return {
        'app': server,
        'db': db
    }
