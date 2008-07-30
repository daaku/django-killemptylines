"""
KillEmptyLines Middleware
"""

import re
from django.conf import settings

NEWLINES = re.compile(r'\s*[\n\r]+')

class KillEmptyLines:
    def process_response(self, request, response):
        if 'text/html' not in response['Content-Type']:
            return response
        if request.is_ajax():
            return response
        if not settings.DEBUG:
            return response

        response.content = NEWLINES.sub('\n', response.content)
        return response
