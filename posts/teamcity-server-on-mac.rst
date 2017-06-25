.. title: TeamCity Server on Mac
.. slug: teamcity-server-on-mac
.. date: 2016-12-14 18:47:35 UTC-08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text

Setting up a TeamCity Server on Mac as a personal agent was very easy.

1. Run TeamCity server

.. code-block:: bash

    #!/bin/bash

    PATH_TO_DATA_DIR=/Users/senthil/teamcity/data
    PATH_TO_LOGS_DIR=/Users/senthil/teamcity/logs
    PORT_HOST=8111

    docker run -it --name teamcity-server-instance  \
        -v $PATH_TO_DATA_DIR:/data/teamcity_server/datadir \
        -v $PATH_TO_LOGS_DIR:/opt/teamcity/logs  \
        -p $PORT_HOST:8111 \
        jetbrains/teamcity-server


The teamcity server is accessible now at http://127.0.0.1:8111

2. Setup a reverse proxy to access that locally.

.. code-block:: bash

    $ cat /etc/apache2/vhosts/teamcity.local.conf
    <VirtualHost *:80>
        ProxyPreserveHost On
        ServerName teamcity.local
        ProxyPass / http://127.0.0.1:8111/
        ProxyPassReverse / http://127.0.0.1:8111/
        LogLevel debug
    </VirtualHost>

3. Setup your `/etc/host` to point http://teamcity.local to 127.0.0.1:8111

.. code-block:: bash

    $ cat /etc/hosts |grep teamcity
    127.0.0.1   teamcity.local




