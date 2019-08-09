Prerequisites for Scripts:

1.  Ensure you have Python version 2: run `python --version`

2.  Install Git for Python :
https://gitpython.readthedocs.io/en/stable/intro.html#installing-gitpython

3.  Setup Acquia aliases

------------
 ## Drush Maker

drush_maker.py -- help article 
 
 
 Run as below: 
 
 if make file is in current directory 
 
 `python drush_maker.py` 
 
 provide target path (this should be a git repo)
 
 `python drush_maker.py /path/to/repo/` 
 
 ------------
 ## Simple Tasks
 
 `python simple_task.py --help`
 
 
`action  [ coder | otl | otl_docs | db_dump ]`

`subscription  Subscription of the site`

`environment [ dev | test ]`

OR `debug_ssh` to solve ssh-agent issue

---------------
## Box Mover
Install Box API sdk for Python:
> pip install boxsdk

Dev token:

https://developer.box.com/docs/authenticate-with-developer-token