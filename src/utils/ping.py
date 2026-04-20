import subprocess
def ping_device(ip):
    result = subprocess.run(["ping","-c","1",ip],stdout = subprocess.PIPE,stderr = subprocess.PIPE)
    if result.returncode==0:
        return True
    else:
        return False
