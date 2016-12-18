import canvaslms.api as api
import json

def connect_server(tokenLocation, server):

    authToken = api.getAuthTokenFromFile('auth-token.txt')

    conn = api.CanvasAPI('canvas.wpi.edu', authToken)

    return conn

def list_classes(conn):
    classes = {}
    results = conn.allPages('courses')

    for i in range(len(results)):
        try:
            classes[results[i]['name']] =  results[i]['id']
        except KeyError as e:
           pass

    return(classes)

if __name__ == "__main__":
    conn = connect_server('auth-token.txt', 'canvas.wpi.edu')

    classes = list_classes(conn)

    print(classes)




