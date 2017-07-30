# _*_ coding:utf-8 _*_

import xadmin

from courses.models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'course_org', 'learn_times', 'degree',
                    'add_time']
    search_fields = ['name', 'desc', 'detail', 'course_org', 'learn_times', 'degree']
    list_filter = ['name', 'desc', 'detail', 'course_org', 'learn_times', 'degree', 'students', 'click_num',
                   'fav_num', 'add_time']


class LessonAdmin(object):
    list_display = ['course', 'name', 'learn_time', 'add_time']
    search_fields = ['course', 'name', 'learn_time']
    list_filter = ['course__name', 'name', 'learn_time', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'url', 'add_time']
    search_fields = ['lesson', 'name', 'url']
    list_filter = ['lesson', 'name', 'url', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
