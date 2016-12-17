import canvaslms.api as api


authToken = api.getAuthTokenFromFile('auth-token.txt')

apiObj = api.CanvasAPI('canvas.wpi.edu', authToken)

results = apiObj.allPages('courses')

print(results)

