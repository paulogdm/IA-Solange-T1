blind:
	@python3.4 blind_search.py map1.bmp

install_ubuntu:
	sudo apt-get install python-pip
	$(MAKE) install_pillow

install_arch:
	sudo pacman -S python-pip --needed
	$(MAKE) install_pillow

install_pillow:
	sudo pip3.4 install pillow
