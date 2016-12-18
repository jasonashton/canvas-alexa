import canvaslms.api as api
import json

def connect_server(tokenLocation, server):

    authToken = api.getAuthTokenFromFile('auth-token.txt')

    conn = api.CanvasAPI('canvas.wpi.edu', authToken)

    return conn

if __name__ == "__main__":
    conn = connect_server('auth-token.txt', 'canvas.wpi.edu')

    results = conn.allPages('courses')

    print(json.dumps(results, sort_keys=True, indent=4))


