import requests
import json

domain = 'write.privacytools.io'

URI = 'https://{}/api/auth/login'.format(domain)
POST_URI = 'https://{}/api/posts'.format(domain)
COLL_URI = 'https://{}/api/collections'.format(domain)
ME_URI = 'https://{}/api/me'.format(domain)

# This is the URI for the Reader of an instance
RWA_URI = 'https://{}/read/api/posts'.format(domain)
