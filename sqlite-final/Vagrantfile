ENV['VAGRANT_SERVER_URL'] = 'https://vagrant.elab.pro'
# Указали зеркало ,потому что напрямую через vagrant без использования прокси скачать нельзя

Vagrant.configure("2") do |config|
  # 2 в скобочке это версия vagrant  (от 1.1 до современных), если ввести 1 будет первая версия , где команды отличаются от текущих
  config.vm.box = "debian/bullseye64"

  # Параметры виртуальной машины
  config.vm.provider "virtualbox" do |vb|
    vb.name = "sqlite_build_debian"
    vb.memory = "1024"
    vb.cpus = 1
    vb.gui = false
    # запускать без окна в фоне
  end

  # Синхронизировали папку на нашем пк и на виртуалке 
  config.vm.synced_folder ".", "/home/vagrant/project"

  # Через командную строку настраиваем нашу вм , т.е запускаем bash 
  config.vm.provision "shell", inline: <<-SHELL
  #  Удаляем проблемный репозиторий backports
  rm -f /etc/apt/sources.list.d/backports.list
    sed -i '/backports/d' /etc/apt/sources.list
  # дебиан ругается на то, что у нас не совпадает время , немного поправили
  echo 'Acquire::Check-Valid-Until "false";' > /etc/apt/apt.conf.d/99no-check-valid-until
  hwclock -s
    apt-get update
    apt-get install -y build-essential cmake unzip
  SHELL

  # Разварачиваем playbook для 6 задания
  # ansible_local т.к. запускаем ansible в debian
  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "dockerplaybook.yml"
    ansible.provisioning_path = "/home/vagrant/project"
    # Указываем, чтобы ansible установился сам внутри Debian
    ansible.install = true 
  end

end