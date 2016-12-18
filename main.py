import canvaslms.api as api
import json

def connect_server(tokenLocation, server):

    authToken = api.getAuthTokenFromFile('auth-token.txt')

    conn = api.CanvasAPI('canvas.wpi.edu', authToken)

    return conn

def list_classes(conn):
    results = conn.allPages('courses')

    for i in range(len(results)):
        try:
            print("{}, {}".format(results[i]['name'], results[i]['id']))
        except Exception as e:
            print('Unlisted')

if __name__ == "__main__":
    conn = connect_server('auth-token.txt', 'canvas.wpi.edu')

    list_classes(conn)




