#!/bin/sh
# Remove the backslash before running this script
basemachine=\$HOME/PycharmProjects/basemachine
inventory=$basemachine/.vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory
privatekey=$basemachine/.vagrant/machines/default/virtualbox/private_key

ansible-playbook -u vagrant -i $inventory --private-key=$privatekey --extra-vars="@deployvarsdev.json" playbook.yml
