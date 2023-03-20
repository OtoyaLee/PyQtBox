import subprocess

class ADBCommand:
    def __init__(self, cmd):
        self.cmd = cmd
    
    def execute(self):
        adb_output = subprocess.check_output(self.cmd, shell=True)
        return adb_output.decode()
