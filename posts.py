import requests
import json
import code

class post(object):
    def __init__(self, domain):
        self.uri = 'https://{}/api/posts'.format(domain)

    def get(self, id):
        p = requests.get(self.uri + "/%s" % id,
                headers={"Content-Type":"application/json"})

        if p.status_code != 200:
            return "Error in retrievePost(): %s" % p.json()["error_msg"]

        else:
            post = p.json()["data"]
            return post

    def create(self, token, body, title):

        data = {"body": body,
                "title": title}

        p = requests.post(self.uri, data=json.dumps(data),
                    headers={"Authorization": "Token %s" % token,
                        "Content-Type":"application/json"})

        if p.status_code != 201:
            return "Error in createPost(): %s" % p.json()["error_msg"]

        else:
            post = p.json()["data"]
            return post

    def update(self, token, id, **kwargs):
        data = json.dumps(kwargs)

        p = requests.post(self.uri + "/%s" % id, data=data,
            headers={"Authorization": "Token %s" % token,
                    "Content-Type":"application/json"})

        if p.status_code != 200:
            return "Error in updatePost(): %s" % p.json()["error_msg"]

        else:
            post = p.json()
            return post

    def delete(self, token, id):

        p = requests.delete(self.uri + "/%s" % id,
            headers={"Authorization": "Token %s" % token,
                    "Content-Type": "application/json"})

        if p.status_code != 204:
            return "Error in deletePost(): Invalid token or post doesn't exist under your account."

        else:
            return "Post deleted!"

    def claim(self, token, id, ptoken):
        data = [{"id": id,
                "token": ptoken}]

        p = requests.post(self.uri + "/claim", data=json.dumps(data),
            headers={"Authorization": "Token %s" % token,
                    "Content-Type": "application/json"})

        if p.status_code != 200:
            return "Error in claimPost(): %s" % p.json()["error_msg"]

        else:
            post = p.json()["data"]
            return post
