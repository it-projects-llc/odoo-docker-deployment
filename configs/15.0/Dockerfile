FROM odoo:15.0
USER root
RUN apt-get update

RUN apt-get install -y build-essential libssl-dev libffi-dev python3-dev cargo
RUN python -m pip install pip --upgrade
# RUN python3 -m pip install pysftp
# RUN python3 -m pip install viberbot
# RUN python3 -m pip install python-telegram-bot

COPY ./adminpwd.patch /tmp/adminpwd.patch
RUN patch -p1 -d /usr/lib/python3/dist-packages -i /tmp/adminpwd.patch

USER odoo
