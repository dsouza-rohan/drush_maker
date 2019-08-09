import os
import sys
import time
import zipfile
import datetime


class BoxMover:
    """Simple Box API class"""

    path = ""
    tags = ""
    folder_name = ""

    def __init__(self, mode):
        self.mode = mode
        self.local_dir = ""
        self.plugin_path = os.getcwd() + "/" + self.local_dir

    def __del__(self):
        print "Script done!!"

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

    def move_to_box(self, full_repo_path):

        print "Create Zip file.. \nPlease Enter y/n"
        progress = raw_input()
        if progress == 'y':
            # zip the folder
            to_zip_dir = self.plugin_path + self.folder_name
            zip_stout = self.gzip_local_folder(to_zip_dir, self.folder_name)
            print zip_stout

        else:
            print "Script ended!!"


def runner_handler(event):
    if len(event) > 0:
        fc = BoxMover
        #  pass target folder/repo to script
        fc.move_to_box(BoxMover("todo"), event['path'])


# Local testing


print sys.argv

if len(sys.argv) > 1:
    event_local = {'path':  sys.argv[1]}
    runner_handler(event_local)
else:
    event_local = {'path': ""}
    runner_handler(event_local)




