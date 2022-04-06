# ----------------------------------------------------------------
# Author:Dylan Intriago
# Date:06/04/2022
#
# This module supports changes in the registered courses
# for students in the class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for.
# -----------------------------------------------------------------
student_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')]
course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5, 'CSC104': 3}
course_roster = {'CSC101': ['1004', '1003'], 'CSC102': ['1001'], 'CSC103': ['1002'], 'CSC104': []}
course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1, 'CSC104': 3}

def list_courses(id, c_roster):
    CSC101 = course_roster['CSC101']
    CSC102 = course_roster['CSC102']
    CSC103 = course_roster['CSC103']
    CSC104 = course_roster['CSC104']
    total_classes = 0
    print('Course registered:')
    if id in CSC101:
        print('CSC101')
        total_classes += 1
    if id in CSC102:
        print('CSC102')
        total_classes += 1
    if id in CSC103:
        print('CSC103')
        total_classes += 1
    if id in CSC104:
        print('CSC104')
        total_classes += 1
    print('Total number:', total_classes)


def add_course(id, c_roster, c_max_size):
    course_add = input('Enter what course you want to add: ')
#Checking for if the course is avaliable
    if course_add not in course_roster.keys():
        print('Course not found')
#Checking if the student has already been enrolled in that course
    CSC101 = course_roster['CSC101']
    CSC102 = course_roster['CSC102']
    CSC103 = course_roster['CSC103']
    CSC104 = course_roster['CSC104']
    if course_add in 'CSC101':
        if id in CSC101:
            print('You have already been enrolled in that course.')
            return()
    if course_add in 'CSC102':
        if id in CSC102:
            print('You have already been enrolled in that course.')
            return()
    if course_add in 'CSC103':
        if id in CSC103:
            print('You have already been enrolled in that course.')
            return()
    if course_add in 'CSC104':
        if id in CSC104:
            print('You have already been enrolled in that course.')
            return()
#Checking for how full the class is
    if course_add in 'CSC101':
        if len(CSC101) > course_max_size['CSC101']:
            print('This class is full.')
            return()
    if course_add in 'CSC102':
        if len(CSC102) > course_max_size['CSC102']:
            print('This class is full.')
            return()
    if course_add in 'CSC103':
        if len(CSC103) > course_max_size['CSC103']:
            print('This class is full.')
            return()
    if course_add in 'CSC104':
        if len(CSC104) > course_max_size['CSC104']:
            print('This class is full.')
            return()
#adding the course to the list
    course_roster[course_add] += [id]
    print('Course added.')


def drop_course(id, c_roster):
    course_drop = input('Enter what course you want to drop: ')
    if course_drop not in course_roster.keys():
        print('Course not found')

    CSC101 = course_roster['CSC101']
    CSC102 = course_roster['CSC102']
    CSC103 = course_roster['CSC103']
    CSC104 = course_roster['CSC104']
    if course_drop in 'CSC101':
        if id not in CSC101:
            print('You are not enrolled in that course.')
            return()
    if course_drop in 'CSC102':
        if id not in CSC102:
            print('You are not enrolled in that course.')
            return()
    if course_drop in 'CSC103':
        if id not in CSC103:
            print('You are not enrolled in that course.')
            return()
    if course_drop in 'CSC104':
        if id not in CSC104:
            print('You are not enrolled in that course.')
            return()

    course_roster[course_drop].remove(id)
    print('Course Dropped.')

