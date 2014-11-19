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

Fedora Cloud builds on Koji
---------------------------

Use `this link <http://koji.fedoraproject.org/koji/tasks?start=0&state=closed&view=flat&method=createImage&order=-id>`_ to
find Fedora Cloud builds on Koji.

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

    # ./dobuild.sh fedora-cloud-base-1dddaee.ks

Why the kickstart file used by Fedora koji looks different?
###########################################################

Because before the installation *ksflatten* command creates an unified kickstart file which has all included kickstart files.

For example run this command in the sphin-kickstarts git repo to create a latest kickstart file::

    $  ksflatten -c fedora-cloud-base.ks -o fedora-cloud-base-$(git rev-parse --short HEAD).ks >& /dev/null


Important files
###############

dobuild.sh

    This is the shell script to simplify life.

fedora-cloud-base-\*.ks

    The kickstart file used to do the actual build.

tdl-x86_64.xml

    The XML schema required for the imagefactory. The koji imagefactory is a patched package which does not need any **rootpw**, but we do need it here. To learn more about the XML tags, you can view `this guide <http://imgfac.org/documentation/tdl/TDL.html>`_


.. note::
   You will find diffrent kind of URL(s) used for the koji builds of the same cloud images. Like *http://compose-x86-02.phx2.fedoraproject.org/compose/21_Beta_RC2/21_Beta/Cloud/x86_64/os/* which is actually the local host where the compose run and after all the processes are done and verified, it is synced to a public repo like *http://dl.fedoraproject.org/pub/alt/stage/21_Beta_RC2/Cloud/x86_64/os/*. 

Disabling root password
#########################

You can configure imagefactory to disable any root password in the template. You have to do it in */etc/imagefactory/imagefactory.conf*, change the value of *tdl_require_root_pw* to 0.

How to create a qcow2 image?
----------------------------

Like the example below::

    $ /usr/bin/qemu-img convert -c -f raw -O qcow2 /var/tmp/koji/tasks/8932/7978932/output_image/3f009dd2-e488-4bb2-960a-5c3765241bad.body /var/tmp/koji/tasks/8932/7978932/Fedora-Cloud-Base-20141029-21_Beta.x86_64.qcow2

How to test a koji image in your local computer?
-------------------------------------------------

There are many different ways one can run and test the Fedora cloud images built on koji.fedoraproject.org. I am going to talk
about a simple script written by Mike Ruckman. First checkout the latest version of the code from github.::

    $ git clone https://github.com/Rorosha/testCloud.git

You will also have to install *libguestfs-tools-c* package using yum.::

    $ yum install libguestfs-tools-c -y


Now inside the directory there is a script called *testCloud.py*, we will use this along with an URL to a cloud image.::

    $ ./testCloud.py --ram 2048 --no-graphic https://kojipkgs.fedoraproject.org//work/tasks/8933/7978933/Fedora-Cloud-Base-20141029-21_Beta.i386.qcow2

As you can see I gave 2GB ram to that test instance. After this you can simply login to the instance using ssh.::

    $ ssh -F ./ssh_config testCloud

The default password is **passw0rd**.

List of current tests for Fedora Cloud image
---------------------------------------------

This `wiki page <https://fedoraproject.org/wiki/Test_Results:Current_Cloud_Test>`_ contains all the latest tests to run on Fedora Cloud images.

How to run Kushal's personal cloud tests?
------------------------------------------

I have a set of tests for the cloud images, they are available in cloudtests directory. First start an instance locally using testCloud as shown above or create an instance in a remote Openstack/Eucalyptus/AWS account. To run the tests in the local
system just give the following command::

    $ ./runlocal.sh

For the remote systems you have to provide the instance IP like in the following example.::

    $ ./runremote.sh 192.168.1.2


.. note:: We need fabric to run these tests. You can install it using yum. *# yum install fabric -y*
