FAQ
====

All the random questions that comes in my mind or people ask me :)

How to move between terminals in text mode installation using Anaconda?
-----------------------------------------------------------------------

Ctrl + B, 2

Why there is a separate compose tree for Cloud?
-----------------------------------------------

Not very clear but someone from community or rel-eng thought that it is a good idea. Of course
this might help in future. The tree is generated from `this <https://git.fedorahosted.org/cgit/spin-kickstarts.git/tree/fedora-install-cloud.ks>`_
kickstart file.

From where I can learn more about Kickstart files?
---------------------------------------------------

Read `this wiki <http://fedoraproject.org/wiki/Anaconda/Kickstart>`_ page.

How to map remote VNC ports to the localhost?
---------------------------------------------

You can do it with help from *ssh* tool. The following command maps three remote ports in the localhost, which you can use to view in a vnc viewer. The local ports are 5800, 5801, 5802

::

    $ ssh root@your_remote_host -L 5800:localhost:5900 -L 5801:localhost:5901 -L 5802:localhost:5902 -L 5803:localhost:5903

