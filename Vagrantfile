# set up the default terminal
ENV["TERM"]="linux"

# set minimum version for Vagrant
Vagrant.require_version ">= 2.2.10"
Vagrant.configure("2") do |config|
  
  # Set the image for the vagrant box
  config.vm.box = "bento/ubuntu-20.04"

  # Set the static IP for the vagrant box
  config.vm.network "private_network", ip: "192.168.50.4"
  
  config.vm.boot_timeout = 600
  
  # Configure the parameters for VirtualBox provider
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "4096"
    vb.cpus = 4
    vb.customize ["modifyvm", :id, "--ioapic", "on"]
  end
end
