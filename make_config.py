#!/usr/bin/env python3
import os
import sys

TEMPLATES = ["nginx.conf.template", "docker-compose.yml.template"]

try:
    ODOO_PORT = os.environ["ODOO_PORT"]
    LONGPOLLING_PORT = os.environ["LONGPOLLING_PORT"]
except KeyError as e:
    print("Не задано переменное окружение: {}".format(e), file=sys.stderr)
    sys.exit(1)

for input_filename in TEMPLATES:
    with open(input_filename, "r") as f:
        config = f.read()

        config = config.replace("ODOO_PORT", ODOO_PORT)
        config = config.replace("LONGPOLLING_PORT", LONGPOLLING_PORT)

        output_filename = input_filename.replace(".template", "")
        with open(output_filename, "w") as f:
            f.write(config)
