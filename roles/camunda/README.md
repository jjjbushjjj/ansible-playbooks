Camunda
=========

The general role for camunda installation
Just basic things without any customization

Requirements
------------

jre or jdk on the box

Role Variables
--------------

Default variables for role:

camunda_platform: tomcat 
App server platform only tomcat is supported atm

camunda_ver: 7.8 
Camunda release version. Also role supports upgrades and downgrades. But do it in very radical way,
if it founds allready deployed installation with version other than this one. It completly REMOVES
all from base directory and installs version you put here. There is a warning for this with a chance to abort.

camunda_remove_examples: False
Remove or not examples and tomcat manager apps se complete list below

camunda_example_apps:
  - camunda-invoice
  - camunda-welcome
  - engine-rest
  - examples
  - host-manager
  - manager
  - ROOT
  - doc
  - h2
This will be removed if you turn on camunda_remove_examples to True

camunda_archive: "camunda-bpm-{{camunda_platform}}-{{camunda_ver}}.0.tar.gz"
Archive name to download

camunda_dist_url: "https://camunda.org/release/camunda-bpm/{{camunda_platform}}/{{camunda_ver}}/{{camunda_archive}}"
Url with archive

camunda_install_dir: "/opt/camunda"
Base installation catalog

camunda_user: camunda
camunda_group: camunda
User and group that's running process

camunda_tomcat_xms: 128M 
camunda_tomcat_xmx: 765M 
Tomcat memory customization

All variables are defined in defaults if you want to override them, do it in your inventory

Dependencies
------------

Java working on the box

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: camunda }

License
-------

BSD

Author Information
------------------

Bushuev A.V.
