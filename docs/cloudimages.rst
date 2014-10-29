Notes related to the Fedora Cloud images
=========================================

This section contains my worknotes related to the Fedora cloud images.

Kickstart files
---------------

Fedora kickstart files are in a git repository. You can use the following command to clone them.::

    $ git clone https://git.fedorahosted.org/git/spin-kickstarts.git


Release engineering scripts
---------------------------

Fedora release engineering team has many scripts for their work. These scripts are available at the following git repo.::

    $ git clone https://git.fedorahosted.org/git/releng

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

Why the kickstart file used by Fedora koji looks different?
###########################################################

Because before the installation *ksflatten* command creates an unified kickstart file which has all included kickstart files.

For example run this command in the sphin-kickstarts git repo to create a latest kickstart file::

    $  ksflatten -c fedora-cloud-base.ks -o fedora-cloud-base-$(git rev-parse --short HEAD).ks >& /dev/null


Important files
###############

dobuild.sh

    This is the shell script to simplify life.

koji-\*.ks

    The kickstart file used to do the actual build.

tdl-x86_64.xml

    The XML schema required for the imagefactory. The koji imagefactory is a patched package which does not need any **rootpw**, but we do need it here. To learn more about the XML tags, you can view `this guide <http://imgfac.org/documentation/tdl/TDL.html>`_


.. note:: Difference between different repo URL(s)
   You will find diffrent kind of URL(s) used for the koji builds of the same cloud images. Like **http://compose-x86-02.phx2.fedoraproject.org/compose/21_Beta_RC2/21_Beta/Cloud/x86_64/os/** which is actually the local host where the compose run and after all the processes are done and verified, it is synced to a public repo like **http://dl.fedoraproject.org/pub/alt/stage/21_Beta_RC2/Cloud/x86_64/os/**. 
