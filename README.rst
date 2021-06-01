====================================================
Разворачивание odoo сервера с помощью docker-compose
====================================================

Перед тем как начать
--------------------

- Устанавливаем git.
  Обычно через команду ``sudo apt-get install git``.

- Редактируем ``nginx.conf``.
  Напротив server_name перечисляем через домены, которые будут использоваться

- Редактируем ``Dockerfile``.
  Поправляем версию Odoo, если требуется.

- Выставляем переменные окружения

.. code-block:: sh

   export ODOO_VERSION=14.0  # Используем его для выполнения каких-либо команд данной инструкции.
   export ODOO_DATABASE=mycompany  # название базы, в котором все будем устанавливать

- Выставляем владельца на каталог backups:

.. code-block:: sh

   sudo chown 101:101 backups

- В каталоге ``vendor`` клонируем репозитории с модулями.
  Среди обязательных это репозиторий с auto_backup.

.. code-block:: sh

   cd vendor
   git clone https://github.com/Yenthe666/auto_backup.git -b $ODOO_VERSION --single-branch

- Редактируем ``odoo.conf``.
  Выставляем нужные параметры.
  Среди них:

  - список каталогов с модулями.
    Для ``auto_backup`` каталог уже добавлен, а для остальных делаем по примеру.

  - ``admin_password``.
    Оставлять стандартным не рекомендую.

Установка docker и docker-compose
---------------------------------

Для Debian подготовлен скрипт ``install_docker_debian.sh``.

Для других операционных систем надо смотреть тут https://docs.docker.com/engine/install/ и тут https://docs.docker.com/compose/install/

Установка nginx
---------------

Для Debian и Ubuntu подобных

.. code-block:: sh

   sudo apt-get install nginx


Установка certbot
-----------------

Не требуется, если у клиента есть свой сертификат и сам будет его обновлять.

.. code-block:: sh

   sudo apt-get install certbot

Настройка nginx
---------------

Есть готовый шаблон.

.. code-block:: sh

   sudo cp ./nginx.conf /etc/nginx/sites-available/odoo.conf
   sudo ln -s /etc/nginx/sites-available/odoo.conf /etc/nginx/sites-enabled/odoo.conf

Убеждаемся, что все правильно настроили:

.. code-block:: sh

   sudo nginx -t

Если на выводе будет что-то вроде "все ок", то продолжаем.
Если нет, то исправляем ошибки и после чего продолжаем.

.. code-block:: sh

   sudo service nginx restart

Привязка сертификата от Let's Encrypt
-------------------------------------

Выполняем команду ниже и отвечаем на вопросы

.. code-block:: sh

   sudo certbot

Разворачивание odoo
-------------------

В новой базе сразу устанавливаем ``auto_backup``

.. code-block:: sh

   sudo docker-compose run --rm web odoo -d $ODOO_DATABASE -i auto_backup --stop-after-init

Убеждаемся, что ошибок никаких не было.

Далее снова запускаем Odoo без привязки с консоли:

.. code-block:: sh

   sudo docker-compose up -d web

Открываем браузер, заходим в Odoo

- Логин: admin, пароль: admin
- Основное меню >> Settings >> Activate developer mode
- Основное меню >> Settings >> Technical >> Configure back-ups
- Create
- Параметры по-умолчанию заданы корректно. Save
- Technical >> Scheduled Actions
- Открываем Backup scheduler
- Нажимаем на "Run manually"
- При успехе в каталоге backups будет создан дамп
- Переключаем значение поле Active. Должно иметь состояние "Включено"

Готово. Дальше уже устанавливаем нужные модули, настраиваем пользователей и прочее
