run:
	./run.sh

install_ubuntu:
	sudo apt-get install python-pip
	$(MAKE) install_pillow

install_arch:
	sudo pacman -S python-pip --needed
	$(MAKE) install_pillow

install_pillow:
	sudo pip3.4 install pillow
