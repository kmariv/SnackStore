# SnackStore

** IMPORTANT 
	--> You should have python 2.7.6  
	--> Create an environment in Linux OS.

** Install the environment:

	1) Create a virtualenv 
		1.1) Install pip tool 
			1.1.1) Download get-pip.py
				https://bootstrap.pypa.io/get-pip.py
			1.1.2) Go to the directory where get-pip.py is and execute in a terminal:
				sudo python get-pip.py.sudo
				
		1.2) Install Virtualenv --->  Execute in a terminal
			1.2.1) sudo pip install virtualenv
			1.2.2) sudo pip install virtualenvwrapper
			1.2.3) WORKON_HOME=~/Envs
			1.2.4) source /usr/local/bin/virtualenvwrapper.sh
			1.2.5) mkvirtualenv snackenv
			1.2.6) workon snackenv
			
			You should edit the file /home/<username>/.bashrc and add the lines 1.2.3) and 1.2.4) to keep working with "workon"
				
	2) Install the environment:
		[NOTE]: Be sure you are into the virtualenv
		
		Execute in a terminal:
			pip install -r requirements.txt
