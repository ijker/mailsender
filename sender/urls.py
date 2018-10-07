# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(
    'sender.views',
    (r'^$', 'home'),
    (r'^send/$','sendmail'),
)
