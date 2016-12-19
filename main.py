import class_conn
if __name__ == "__main__":
    #Algo: 1843
    #Exam2: 2421

    classes = class_conn.canvasConn()
    for i in classes.list_classes_id():
        classes.print_last_submission(i)




