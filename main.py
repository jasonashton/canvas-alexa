import class_conn
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
def launched():
    return question('Welcome to Jason\'s Canvas app. Say: get my recent grades or quit')

@ask.intent("RecentGradesIntent")
def get_recent_grades(course = ''):

    classes = class_conn.canvasConn()

    classes_statement = '<speak> '

    if course:
        class_id = classes.name_to_id(course)
        classes_statement += classes.print_last_submission(class_id)
    else:
        for i in classes.list_classes_id():
            classes_statement += classes.print_last_submission(i)

    classes_statement += ' </speak>'

    print(classes_statement)
    return statement(classes_statement)


if __name__ == "__main__":
    app.run(debug=True)
