#!/usr/bin/python3
""" deploy web static"""

from fabric.api import put, run, env
import os
import tarfile
env.hosts = ['34.75.234.107', '3.84.184.141']


def do_deploy(archive_path):
    """distributes an file to the web servers"""
    if os.path.exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        sin_ext = file_name(".")[0]
        put(archive_path, "/tmp/")
        ruta = "/data/web_static/releases/"
        run("tar -xzf {}{} {}".format(ruta, sin_ext, file_name))
        run("sudo rm -f /tmp/{}".format(file_name))
        run("sudo rm -rf /data/web_static/current")
        run("ln -sf {}{} /data/web_static/current".format(ruta, sin_ext))

        return True
    except:
        return False
