import canvaslms.api as api
import json
from datetime import datetime


class canvasConn:

    def __init__(self, tokenLocation='auth-token.txt', server='canvas.wpi.edu'):
        self.tokenLocation = tokenLocation
        self.server = server

        self.conn = api.CanvasAPI(server, api.getAuthTokenFromFile(tokenLocation))


    '''
        Returns IDs of classes in list
    '''
    def list_classes_id(self):
        classes = []
        results = self.conn.allPages('courses')

        for i in range(len(results)):
            if 'name' in results[i]:
                classes.append(results[i]['id'])

        return(classes)


    '''
    Returns ID of last updated assignment
    '''
    def get_last_asst(self, class_id):
        results = self.conn.allPages('courses/{}/assignments'.format(class_id))

        recent_index = 0
        recent_time = datetime.strptime(results[0]['updated_at'], '%Y-%m-%dT%H:%M:%SZ')

        for i in range(len(results)):
            time = datetime.strptime(results[i]['updated_at'], '%Y-%m-%dT%H:%M:%SZ')

            if time > recent_time:
                recent_time = time
                recent_index = i

        return int(results[recent_index]['id'])


    '''
        Get last grade for an assignment
    '''
    def get_asst_grade(self, class_id, asst_id):
        results = self.conn.allPages('courses/{}/assignments/{}/submissions/self'.format(class_id, asst_id))
        score = results[-1]['score']
        if score is not None:
            return float(score)

    def print_last_submission(self, class_id):
        course = self.conn.allPages('courses/{}'.format(class_id))[0]['name']

        asst_id = self.get_last_asst(class_id)

        asst = self.conn.allPages('courses/{}/assignments/{}'.format(class_id, asst_id))[0]

        asst_name = asst['name']
        asst_total = asst['points_possible']

        grade = self.get_asst_grade(class_id, asst_id)

        return('<p>{}:<break strength="strong" /> Last Assignment Updated: {} <break strength="strong" />Grade: <say-as interpret-as="unit">{}</say-as><break strength="weak" /> out of <say-as interpret-as="unit">{}</say-as></p>'.format(course, asst_name, grade, asst_total))


    def name_to_id(self, name):
        classes = self.list_classes_id()
        name = name.lower()

        for i in classes:
            class_name = self.conn.allPages('courses/{}'.format(i))[0]['name'].lower()
            if name in class_name:
                return i
