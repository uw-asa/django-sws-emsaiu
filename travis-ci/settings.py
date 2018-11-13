import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

DEBUG = True

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'compressor',
    'supporttools',
    'uw_saml',
    'emsaiu',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.PersistentRemoteUserMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.RemoteUserBackend',
]

ROOT_URLCONF = 'travis-ci.urls'

WSGI_APPLICATION = 'travis-ci.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
            ],
        },
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = ''
STATIC_URL = '/static/'

EMSTOOLS_SCHEDULER_GROUP = 'u_classrm_services_ems_schedulers'

from django.urls import reverse_lazy
LOGIN_URL = reverse_lazy('saml_login')

UW_SAML = {
    'strict': False,
    'debug': True,
    'sp': {
        'entityId': 'https://example.uw.edu/saml2',
        'assertionConsumerService': {
            'url': 'https://example.uw.edu/saml/sso',
            'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST'
        },
        'singleLogoutService': {
            'url': 'https://example.uw.edu/saml/logout',
            'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect'
        },
        'NameIDFormat': 'urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified',
        'x509cert': '',
        # for encrypted saml assertions uncomment and add the private key
        # 'privateKey': '',
    },
    'idp': {
        'entityId': 'urn:mace:incommon:washington.edu',
        'singleSignOnService': {
            'url': 'https://idp.u.washington.edu/idp/profile/SAML2/Redirect/SSO',
            'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect'
        },
        'singleLogoutService': {
            'url': 'https://idp.u.washington.edu/idp/logout',
            'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect'
        },
        'x509cert': '',
    },
    'security': {
        # for encrypted saml assertions
        # 'wantAssertionsEncrypted': True,
        # for 2FA uncomment this line
        # 'requestedAuthnContext':  ['urn:oasis:names:tc:SAML:2.0:ac:classes:TimeSyncToken']
    }
}

MOCK_SAML_ATTRIBUTES = {
    'uwnetid': ['javerage'],
    'affiliations': ['student', 'member', 'alum', 'staff', 'employee'],
    'eppn': ['javerage@washington.edu'],
    'scopedAffiliations': ['student@washington.edu', 'member@washington.edu'],
    'isMemberOf': ['u_test_group', 'u_test_another_group',
                   'u_classrm_services_ems_schedulers'],
}
