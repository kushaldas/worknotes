This contains random commands I find on internet or things I forget
===================================================================

Comparing files
----------------

comm -13 <(rpm -qla | sort) <(find / -type f | sort) 

Checking for updates
---------------------

* dnf check-update
* yum list updates

Finding rpms with signature
----------------------------

rpm -qa --qf '%{NAME}-%{VERSION}-%{RELEASE} %{SIGPGP:pgpsig} %{SIGGPG:pgpsig}\n'
