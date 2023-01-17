from routes.students import studentRoute


def routing(app):
    app.include_router(studentRoute)