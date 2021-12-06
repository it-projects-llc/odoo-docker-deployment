FROM odoo:13.0
USER root
RUN apt-get update

RUN apt-get install -y build-essential libssl-dev libffi-dev python3-dev cargo
RUN python3 -m pip install xlsxwriter
RUN python3 -m pip install openpyxl

COPY ./adminpwd.patch /tmp/adminpwd.patch
RUN patch -p1 -d /usr/lib/python3/dist-packages -i /tmp/adminpwd.patch

USER odoo
