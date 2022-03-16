FROM odoo:10.0
USER root
RUN apt-get update

RUN apt-get install -y build-essential libssl-dev libffi-dev python-dev cargo

COPY ./adminpwd.patch /tmp/adminpwd.patch
RUN patch -p1 -d /usr/lib/python3/dist-packages -i /tmp/adminpwd.patch

USER odoo
