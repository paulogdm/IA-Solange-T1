run:
	./run.sh

install_ubuntu:
    sudo apt-get install python3
	sudo apt-get install python3-pip
	$(MAKE) install_pillow

install_arch:
    sudo pacman -S python3 --needed
	sudo pacman -S python3-pip --needed
	$(MAKE) install_pillow

install_pillow:
	sudo pip3 install pillow