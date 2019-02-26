# SnackStore

** IMPORTANT:

	--> You should have python 2.7.6 in your OS. 
	--> Create an environment in Linux OS (Preferably Linux Mint )
	--> Session duration: 1 minute

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
			
** How to use:
	
	You can find two folders: snackClient (Front-end) and snackStore (Back-end)
	Please, create a database called "STORE_DB" (current user postgres, current password root) but you can change it in snackStore/snackStore/settings.py
	
	---> You should open two terminal and execute "workon snackenv" in both. 
	
	[ terminal #1 ]
		execute:
			1) cd snackStore
			2) python manage.py runserver 0.0.0.0:8000
			3) Open POSTMAN to prove the API.
		
	[ terminal #2 ]
		execute:
			1) cd snackClient
			2) python manage.py runserver 0.0.0.0:8001
			3) Go to localhost:8001/client/store/
			
** Frameworks, Databases and Other tools USED:

	Python 2.7.6
	Django 1.11
	Django REST Framework
	PostgreSQL (PostgreSQL 9.3.12 on x86_64-unknown-linux-gnu, compiled by gcc (Ubuntu 4.8.4-2ubuntu1~14.04.1) 4.8.4, 64-bit)
	jQuery 1.12.4
	Datatables 1.10.19
	Bootstrap 4
	
	
** HOW TO TEST IT:

	
	Import SnackStore.postman_collection.json in POSTMAN and prove the collection. 

	Also, you can browse into the page: 

			http://localhost:8000/api/getSnacks/

	And prove the list of snacks ;) 


	----> YOU HAVE TO CREATE APPLAUDO USER 
	
		User: applaudo 
		Pass: applaudo

		--- Client (no-admin account)

		User: applaudo_client
		Pass: applaudo


I hope you like it!
