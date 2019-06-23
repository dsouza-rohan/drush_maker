import os
import sys
import time
import zipfile
import datetime
import git
from git import Repo


class drush_maker:
    """Simple Drupal make built class"""

    path = ""
    tags = ""
    folder_name = ""

    def __init__(self, mode):
        self.mode = mode
        self.local_dir = ""
        self.plugin_path = os.getcwd() + "/" + self.local_dir

    def __del__(self):
        print "Script done!!"

    def list_all_branches(self, repo):
        branches = repo.branches
        for branch in branches:
            print branch

    def list_all_tags(self, repo):
        self.tags = repo.tags
        for idx, tag in enumerate(self.tags):
            print "[{}]-> {}".format(idx, tag)

    def do_git_fetch(self, repo):
        for remote in repo.remotes:
            fetch = remote.fetch()
            for fe in fetch:
                print "{}|{}".format(fe.ref, fe.flags)
        print('Repo Git fetch complete..')

    def gzip_local_folder(self, path, file_name):
        # get current date
        now = datetime.datetime.now()
        zip_file_name = self.plugin_path + file_name + "_" + now.strftime("%Y%m%d_%H%M") + '.zip'
        zipf = zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED)
        # Done: add non root target dir to zip file

        # ziph is zipfile handle
        for root, dirs, files in os.walk(path):
            for file in files:
                zipf.write(os.path.join(root, file))

        zipf.close()
        file_stats = os.stat(zip_file_name)

        print "Zip file created name={} size={}\n".format(zip_file_name, file_stats.st_size)

        return zip_file_name

    def make_platform(self, full_repo_path):

        if full_repo_path != "":
            # Todo: check validity of folder
            self.plugin_path = full_repo_path

        print self.plugin_path

        repo = Repo(self.plugin_path)
        git_direct = repo.git

        if not repo.bare:
            print('Repo at {} successfully loaded.'.format(self.plugin_path))

            # run a new git fetch
            self.do_git_fetch(repo)

            # list all tags or lat 10 tags
            self.list_all_tags(repo)

            print "Enter tag number (?) to checkout to.."
            # select 1 tag
            to_tag = int(raw_input())
            print "Confirm checkout to tag -->{}  \nPlease Enter y/n".format(self.tags[to_tag])
            progress = raw_input()

            if progress == 'y':
                # check if exist & checkout to tag/branch
                to_tag_name = self.tags[to_tag]
                git_direct.checkout(to_tag_name)
                print "Checkout done to tag: {}".format(to_tag_name)
                time.sleep(2)

                # run drush
                self.folder_name = "drupal_code_{}".format(str(to_tag_name))
                print "Running drush make, target folder={}".format(self.folder_name)

                # todo: fix drush target folder path
                drush_cmd = "drush make {}drupal.make {} --force-complete".format(self.plugin_path, self.folder_name)
                os.system(drush_cmd)

                print "Create Zip file.. \nPlease Enter y/n"
                progress = raw_input()
                if progress == 'y':
                    # zip the folder
                    to_zip_dir = self.plugin_path + self.folder_name
                    zip_stout = self.gzip_local_folder(to_zip_dir, self.folder_name)
                    print zip_stout

                    print "Please enter the Git user name (User id):- "
                    gitUserName = raw_input()
                    print "Please enter the Acquia Subscription or Git repository name:- "
                    repoName = raw_input()
                    gitCloneUrl = "git@github.com:{}/{}.git".format(str(gitUserName),str(repoName))
                    print "{} \n Please Confirm your Git URL \n Press y/n".format(str(gitCloneUrl))
                    progress = raw_input()
                    if progress == 'y':
                        print "Command Running... \n  git.Git('{}').clone('{}')".format(self.plugin_path, str(gitCloneUrl))
                        git.Git(self.plugin_path).clone(gitCloneUrl)

                else:
                    print "Script ended!!"

            else:
                print "Script ended!!"

        else:
            print('Could not load repository at {} :('.format(self.plugin_path))
            print('Place this file in repository directory..')


def runner_handler(event):
    if len(event) > 0:
        fc = drush_maker
        #  pass target folder/repo to script
        fc.make_platform(drush_maker("todo"), event['path'])


# Local testing


print sys.argv

if len(sys.argv) > 1:
    event_local = {'path':  sys.argv[1]}
    runner_handler(event_local)
else:
    event_local = {'path': ""}
    runner_handler(event_local)
