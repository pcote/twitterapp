# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  # config.vm.box_check_update = false
  # config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "private_network", ip: "192.168.33.10"
  # config.vm.network "public_network"
  
  config.vm.provider "virtualbox" do |vb|
    vb.gui = false 
    vb.memory = "1024"
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
    ansible.extra_vars = "deployvarsdev.json" 
  end
end
