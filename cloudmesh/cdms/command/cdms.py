from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand


class CDMSCommand(PluginCommand):

    @command
    def do_cdms(self, args, arguments):
        """
        ::

          Usage:
                cdms -f FILE
                cdms FILE
                cdms list

          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """
        print(arguments)



