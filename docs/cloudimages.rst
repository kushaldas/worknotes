Notes related to the Fedora Cloud images
=========================================

This section contains my worknotes related to the Fedora cloud images.


Imagefactory
-------------

The cloud images are build using `imagefactory <https://github.com/redhat-imaging/imagefactory>`_ and `oz <https://github.com/clalancette/oz/wiki/Oz-architecture>`_.

I am currently using a Fedora 20 system to do so.

Installation
############

::

    # yum install yum-utils koji-builder strace mock kernel-firmware ntp ntpdate rsyslog oz imagefactory imagefactory-plugins-TinMan imagefactory-plugins-Docker imagefactory-plugins-vSphere imagefactory-plugins-ovfcommon imagefactory-plugins imagefactory-plugins-OVA imagefactory-plugins-EC2 imagefactory-plugins-RHEVM python-psphere VMDKstream pykickstart

Then start the libvirt service.::

    # systemctl start libvirtd


Building your first image
#########################

Next we are going to use imagefactory to build your first image. `Download <https://kushal.fedorapeople.org/f21build.tar.gz>`_ this tar and extract it.

Then just use the following command to build the image.::

    # sh dobuild.sh

Important files
###############

dobuild.sh

    This is the shell script to simplify life.

koji-\*.ks

    The kickstart file used to do the actual build.

tdl-x86_64.xml

    The XML schema required for the imagefactory. The koji imagefactory is a patched package which does not need any **rootpw**, but we do need it here. To learn more about the XML tags, you can view `this guide <http://imgfac.org/documentation/tdl/TDL.html>`_



