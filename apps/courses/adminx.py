# -*- coding:utf-8 -*-
__author__ = 'lx'
__date__ = ' 下午4:47'

from .models import Course, CourseResource, Lesson, Video
import xadmin


class CourseAdmin(object):
    list_display = ['name', 'des', 'detail', 'degree', 'learn_times', 'student']
    search_fields = ['name', 'des', 'detail', 'degree', 'student']
    list_filter = ['name', 'des', 'detail', 'degree', 'learn_times', 'student']


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time', ]
    search_fields = ['course', 'name', ]
    list_filter = ['course__name', 'name', 'add_time', ]


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time', ]
    search_fields = ['lesson', 'name', ]
    list_filter = ['lesson', 'name', 'add_time', ]


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download',  'add_time', ]
    search_fields = ['course', 'name', 'download', ]
    list_filter = ['course', 'name', 'download',  'add_time', ]


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
