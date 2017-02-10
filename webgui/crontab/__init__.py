import subprocess
import re
import os

class Crontab:
    """
    Crontab class.
    Allow to create, remove, disable an enable a Linux crontab line
    """

    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.period = "*"
        self.command = "echo test"
        self.comment = "piclodio"

    def __load(self):
        """ Return a dict of actual crontab """
        # get actual crontab
        p = subprocess.Popen("crontab -l", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        mycron = str(output)
        return mycron.splitlines()

    def __save(self, _newcron):
        """ Write line in a temp file """
        f = open("/tmp/newcron.txt", "w")
        for line in _newcron:
            f.write(line)
            f.write(os.linesep)
        f.close()

        """ Write the temp file into the crontab  """
        # save the crontab from the temp file
        p = subprocess.Popen("crontab /tmp/newcron.txt", stdout=subprocess.PIPE, shell=True)
        p.communicate()

    def __isenable(self):
        """ return True id the cron job line is not commented  """
        # get actual crontab
        mycron = self.__load()

        # locate the line
        for line in mycron:
            if self.comment in line:
                regex = re.compile("^#")
                test = regex.match(line)
                if test:
                    # is disable
                    return False
                else:
                    # is enable
                    return True
        return False

    def create(self):
        """add line to the crontab"""
        # get actual crontab
        mycron = self.__load()

        # add the new line the the end
        line = str(self.minute)+" "+str(self.hour)+" * * "+str(self.period)+" "+str(self.command)+" >/dev/null 2>&1 #"+str(self.comment)
        mycron.append(line)

        # write the crontab
        self.__save(mycron)

    def disable(self):
        """ disable from the crontab. Comment the line into the crontab """
        # get actual crontab
        mycron = self.__load()

        newlist = []

        # locate the line
        for line in mycron:
            if (self.comment in line) and self.__isenable() :
                commentedline = "# "+line
                newlist.append(commentedline)
            else:
                newlist.append(line)

        # write the crontab
        self.__save(newlist)

    def enable(self):
        """ remove comment car ahead the line if present"""
        # get actual crontab
        mycron = self.__load()

        newlist = []

        # locate the line
        for line in mycron:
            if (self.comment in line) and (not self.__isenable()) :
                # extract line without comment
                indexcomment = line.index('#')
                linewithoutcomment = line[indexcomment+2:len(line)]
                newlist.append(linewithoutcomment)
            else:
                newlist.append(line)

        # write the crontab
        self.__save(newlist)

    def remove(self):
        """ Remove the line in the crontab by his comment """
        # get actual crontab
        mycron = self.__load()
        newlist = []

        # locate the line
        for line in mycron:
            if self.comment not in line:
                newlist.append(line)

        # write the crontab
        self.__save(newlist)
