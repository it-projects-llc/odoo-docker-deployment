FROM odoo:13.0
USER root
RUN apt-get update

RUN apt-get install -y build-essential libssl-dev libffi-dev python3-dev cargo

COPY ./adminpwd.patch /tmp/adminpwd.patch
RUN patch -p1 -d /usr/lib/python3/dist-packages -i /tmp/adminpwd.patch

RUN echo "127.0.0.1 services.openerp.com > /etc/hosts"

USER odoo
