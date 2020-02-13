Prerequisites for Scripts:

1.  Ensure you have Python version 3: run `python --version`

2.  Install Git for Python :
https://gitpython.readthedocs.io/en/stable/intro.html#installing-gitpython
https://pypi.org/project/GitPython/

3.  Setup Acquia aliases

4. Install python-docx : https://python-docx.readthedocs.io/en/latest/

5. Install PyYAML: https://pypi.org/project/PyYAML/

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

 To run `otl_doc` command
create a simple_task.yaml file.

---------------

For screen-shot install:

####PyAutoGUI
https://pypi.org/project/PyAutoGUI/

`pip install pyautogui`

####selenium

https://selenium-python.readthedocs.io/installation.html
`pip install selenium`

####Install geckodriver

`brew install geckodriver`

http://macappstore.org/ghostscript/