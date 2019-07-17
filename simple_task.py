import os
import sys
import acapi


class AcqUtility:
    """Simple AcqUtility utility class"""

    action = ""  # action to take
    acq_cli = 0
    acq_sub = ""
    acq_env = ""
    acq_site = 0
    allowed = ["dev", "test", "dev6"]
    pub_key_path = ""
    pub_key_pass = ""
    mode = "drush"  # drush | ssh

    def __init__(self, action, sub, env):
        self.action = action
        self.acq_env = env
        self.acq_sub = sub

        self.local_dir = "../../MyKeys/rohan_ssh2.pem"  # replace with file name
        self.pub_key_path = os.getcwd() + "/" + self.local_dir

        print "start--"

    def __del__(self):
        print "done--"

    def mk_acq_client(self):

        if self.acq_env in self.allowed:

            drush_alias = "@{sub}.{env}".format(sub=self.acq_sub, env=self.acq_env)

            if self.mode == "drush":
                return drush_alias

            elif self.mode == "ssh":
                print "No ssh mode available...yet"
        else:
            print "Connection to {} is not allowed".format(self.acq_env)

            # ==>Available envs are !!
            # for env in envs:
            #     print "Env: {env} SSH Host: {host}".format(env=env, host=envs[env]['ssh_host'])

    def run_scripts(self, action):

        if action == "coder":
            self.mk_coder_report()

        elif action == "otl":
            self.mk_site_uli()

        elif action == "otl_doc":
            print action
            # todo: otl doc script..

        elif action == "db_dump":
            print action
            # todo: db dump...

        elif action == "ssh_agent":
            print action
            self.run_ssh_agent()

        # todo:  and 5x b-fix queries...?

    def mk_coder_report(self):

        alias = self.mk_acq_client()

        os.system("drush {alias} en coder -y".format(alias=alias))
        os.system("drush {alias} coder-review".format(alias=alias))
        os.system("drush {alias} dis coder -y".format(alias=alias))
        os.system("drush {alias} pmu coder -y".format(alias=alias))

        # todo: save coder output to file

    def mk_site_uli(self):

        alias = self.mk_acq_client()

        os.system("drush {alias} uli 1 --no-browser".format(alias=alias))

    def run_ssh_agent(self):
        os.system("eval $(ssh-agent -s)")
        os.system("ssh-add {path}".format(path=self.pub_key_path))


def runner_handler(event):
    if len(event) > 0:
        bf = AcqUtility
        #  pass target folder/repo to script
        bf.run_scripts(AcqUtility(event['action'], event['sub'], event['env']), event['action'])


print sys.argv

if len(sys.argv) == 4:
    event_local = {'action':  sys.argv[1], 'sub':  sys.argv[2], 'env':  sys.argv[3]}
    runner_handler(event_local)
else:
    if len(sys.argv) == 2:
        if sys.argv[1] == "--help":

            print "\n  simple_task.py [action] [subscription] [environment] \n" \
                  " action--> [coder| otl| otl_docs| db_dump ..]\n" \
                  " subscription--> Subscription of the site\n" \
                  " environment--> [dev | test]\n " \
                  "\nOR debug_ssh to solve ssh-agent issue"

        elif sys.argv[1] == "debug_ssh":

            bf = AcqUtility
            bf.run_ssh_agent(AcqUtility(0, 0, 0))

        else:
            print "3 parameters required. Please use --help"
    else:
        print "use --help"

    # Local testing
    event_local = {'action': "", 'sub': "", 'env':  "dev"}
    runner_handler(event_local)

