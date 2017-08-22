###
# Server to accept webhook notifications
# from github and (in-future) push to website
###
import os
import hmac
import json
import hashlib
from tornado import web, ioloop

# I have github_repo_secrets environment variable
# which contains string in this format `key0:value0 keyN:valueN`
# so first read in those values as list and then for simplicity,
# convert each element to a dictionary of key:value pairs
secret_list = os.environ['github_repo_secrets'].split(' ')
MY_SECRETS_DICT = {}
[MY_SECRETS_DICT.update({x.split(':')[0]:x.split(':')[1]}) for x in secret_list]

def check_hash(repository_name, hash_to_compare_with,
               payload, hash_object=hashlib.sha1):
    """
    Compare the `payload` with `hash_to_compare_with`
    using hash_object
    Parameters
    ----------
    repository_name: bytes
        name of repository to generate hash based
        environment value for it
    hash_to_compare_with: bytes
    payload: bytes
    hash_object: `hashlib` object
        default: `hashlib.sha1`
        see hashlib.? for options

    Returns
    -------
    bool
    """
    if repository_name not in MY_SECRETS_DICT.keys():
        return False
    secret = bytes(MY_SECRETS_DICT[repository_name], 'utf-8')
    hm = hmac.new(secret, payload, hash_object)
    return hmac.compare_digest(hash_to_compare_with, hm.hexdigest())
    
class GHHandler(web.RequestHandler):
    """
    Main class for handling post requests from github
    """
    def post(self, *args):
        repo_name = json.loads(self.request.body.decode('utf-8'))['repository']['name']
        sha1_server = self.request.headers.get('X-Hub-Signature').split("sha1=")[-1]
        print("Checking SHA1 for authenticity")
        authentic = check_hash(repo_name, sha1_server, self.request.body)
        print("Authentic? : ", authentic)
        ## do whatever you want with the received message
        
settings = {}

app = web.Application(
    [(r'/ghpayload', GHHandler)],
    **settings
)

if __name__ == "__main__":
    app.listen(8888)
    ioloop.IOLoop.instance().start()
