from django_hosts import patterns, host
from django.conf import settings

host_patterns = patterns('path.to',
    host(r'nexus', 'nexus.urls', name=''),
    host(r'doom', 'doom.urls', name='doom'),
)