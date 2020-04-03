.. title: IPv6 Login
.. slug: ipv6-login
.. date: 2020-04-02 18:34:40 UTC-07:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

It is the year 2021, and I logged into one of my servers using IPv6 address. So far I had struggled with using IPv6
address for anything useful.  Today, I was able login to a server directly from my home using an IPv6 address.

vultr.com provides servers for USD 2.5 per month, with a *restriction* that it will only have IPv6 address.
But if you can ssh to it, why not get those cheap boxes?

::

    $ ssh -6 root@2001:19f0:5401:129f:5400:02ff:fea8:1fde
    The authenticity of host '2001:19f0:5401:129f:5400:2ff:fea8:1fde (2001:19f0:5401:129f:5400:2ff:fea8:1fde)' can't be established.
    ECDSA key fingerprint is SHA256:gcWbxG6LHOBJSssYRJdTfCt9IaRznHqn8iuD2bw3uDo.
    Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
    Warning: Permanently added '2001:19f0:5401:129f:5400:2ff:fea8:1fde' (ECDSA) to the list of known hosts.
    Welcome to Ubuntu 19.10 (GNU/Linux 5.3.0-40-generic x86_64)

     * Documentation:  https://help.ubuntu.com
     * Management:     https://landscape.canonical.com
     * Support:        https://ubuntu.com/advantage

      System information as of Fri 03 Apr 2020 01:28:02 AM UTC

      System load:  0.08              Processes:           96
      Usage of /:   25.8% of 9.78GB   Users logged in:     0
      Memory usage: 31%               IP address for ens3: 100.68.103.207
      Swap usage:   0%


    0 updates can be installed immediately.
    0 of these updates are security updates.


    The list of available updates is more than a week old.
    To check for new updates run: sudo apt update

    root@meet:~#



