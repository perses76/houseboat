from fabric.api import local, settings, abort, run, cd, put, env
from fabric.contrib.project import upload_project

env.hosts = ['oeland.dk']
env.use_ssh_config = True

REMOTE_PROJECT_DIR = '~/projects/houseboat/'


def hello():
    print("Hello world!")


def deploy():
    with cd(REMOTE_PROJECT_DIR):
        upload_project('static', 'static')