FROM odoo:14.0
USER root
RUN apt-get update

RUN apt-get install -y build-essential libssl-dev libffi-dev python3-dev cargo
# RUN python3 -m pip install pysftp
RUN python3 -m pip install viberbot

USER odoo
