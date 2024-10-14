# Import the Canvas class
from canvasapi import Canvas

# Canvas API URL
API_URL = "https://canvas.instructure.com/"
# Canvas API key
API_KEY = "7~tYRfABEynHxxy2cryrQzeLN6DW2BaKzvKcEuB9zmRFXy2nEtBaLYXZAwecVMLcDt"

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)
course = canvas.get_course(10432513)
print(course.name)
user = course.get_user(113770305)
courses = user.get_courses()
print(user.name)
for c in courses:
    print(c)
users = course.get_users()
for user in users:
    print(user.name)
    print(user.id)
    assignments = user.get_assignments(19660357)
    for a in assignments:
        print(a.name)