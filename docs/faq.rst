FAQ
====

All the random questions that comes in my mind or people ask me :)

How can I contribute to the Cloud SIG?
--------------------------------------

There are many ways you can help. The easiest way to start is to test the latest cloud images on your local computer. You can 
use the testCloud application to start an instance in your local system. You can also write your experience in your blog, write
the tips which can save time for others. The Cloud SIG meets every week in #fedora-meeting-1 on freenode at 7pm UTC.

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

How we generate Fedora Docker images?
--------------------------------------

From F21 we are using Fedora Koji builds for Docker. lsm5 takes the .tar.gz image, extracts the rootfs and compress it into a .xz file.
Later that image is published in the Docker hub using github.

How to convert qcow3 images to qcow2?
----------------------------------------

Right now (at least in July, 2015) koji is building version 3 of the qcow2 images. To use them into older systems, you have to convert them into qcow2 images. You can do that with the following command::

    # qemu-img amend -f qcow2 -o compat=0.10 Fedora-Cloud-Base-22-20150521.x86_64.qcow2
