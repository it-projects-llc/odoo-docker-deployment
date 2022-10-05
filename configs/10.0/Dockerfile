FROM odoo:10.0
USER root

RUN rm /etc/apt/sources.list.d/pgdg.list
RUN apt-get update
RUN apt-get install -y apt-transport-https

RUN echo "deb https://apt-archive.postgresql.org/pub/repos/apt jessie-pgdg-archive main" > /etc/apt/sources.list.d/pgdg.list
RUN apt-get update

RUN apt-get install -y build-essential libssl-dev libffi-dev python-dev cargo
RUN python -m pip install --upgrade "pip<21"

COPY ./adminpwd.patch /tmp/adminpwd.patch
RUN patch -p1 -d /usr/lib/python2.7/dist-packages -i /tmp/adminpwd.patch

USER odoo
