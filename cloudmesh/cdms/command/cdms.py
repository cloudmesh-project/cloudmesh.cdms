from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.common.dotdict import dotdict
import subprocess
from subprocess import Popen, PIPE

class CdmsCommand(PluginCommand):

    @command
    def do_cdms(self, args, arguments):
        """
        ::

          Usage:
                cdms [build|run_hadoop|run_omp|clean|realclean]

          This command helps build, run and clean the CDMS application.

          Arguments:
              build       builds the executable
              run_hadoop  runs the hadoop executable
              run_omp     runs the omp executable
              clean       removes object files
              realclean   removes object files and executables

          Options:

        """
        arguments = dotdict(arguments)
        if arguments.build:
            print("Building Executables")
            p = Popen(['.', '/home/cc/intel/bin/compilervars.sh', 'intel64', '&&', 'cd', '/home/cc/cloudmesh.cdms-master/code/trap_analysis', '&&', 'make', 'realclean', '&&', 'make', 'trap_hadoop', '&&', 'make', 'clean', '&&', 'make', 'trap_omp'], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
        elif arguments.run_hadoop:
            print("Running Hadoop Application")
            p = Popen(['echo', './trap_hadoop'], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
        elif arguments.run_omp:
            print("Running OpenMP Application")
            p = Popen(['ls', '-lah'], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
        elif arguments.clean:
            print("Cleaning (skipping executables)")
            p = Popen(['cd', '/home/cc/cloudmesh.cdms-master/code/trap_analysis', ';',  'make', 'clean'], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
        elif arguments.realclean:
            print("Cleaning")
            p = Popen(['cd', '/home/cc/cloudmesh.cdms-master/code/trap_analysis', '&&', 'make', 'realclean'], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
        else: 
            print("error")
            p = Popen(['echo', '...'], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
            
        output, err = p.communicate()
        rc = p.returncode
        if (rc == 0):
            print(output)
        else:
            print(err)
            
