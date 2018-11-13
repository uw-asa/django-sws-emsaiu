import logging
import os
from time import strftime, tzset

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from restclients_core.exceptions import DataFailureException
from uw_saml.decorators import group_required
from uw_sws.term import get_current_term

from emsaiu.exceptions import StudentWebServiceUnavailable

logger = logging.getLogger(__name__)


@group_required(settings.EMSTOOLS_SCHEDULER_GROUP)
def index(request, template='emsaiu/aiu.html'):
    status_code = 200

    try:
        term = get_current_term()
    except DataFailureException as ex:
        logger.exception(ex)
        raise StudentWebServiceUnavailable()

    os.environ['TZ'] = 'America/Los_Angeles'
    tzset()

    context = {
        'term_year': term.year,
        'term_quarter': term.quarter,
        'todays_date': strftime("%Y-%m-%d"),
        'STATIC_URL': settings.STATIC_URL,
    }

    return render(request, template, context, status=status_code)
