#!/usr/bin/python3
"""Fabric script hat distributes an archive to your web servers"""
from fabric.api import put, run, env
from os.path import exists

env.hosts = ["34.75.234.107", "3.84.184.141"]


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        ruta = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('sudo mkdir -p {}{}/'.format(ruta, no_ext))
        run('sudo tar -xzf /tmp/{} -C {}{}/'.format(file_n, ruta, no_ext))
        run('sudo rm /tmp/{}'.format(file_n))
        run('sudo mv {0}{1}/web_static/* {0}{1}/'.format(ruta, no_ext))
        run('sudo rm -rf {}{}/web_static'.format(ruta, no_ext))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {}{}/ /data/web_static/current'.format(ruta, no_ext))
        return True
    except:
        return False
