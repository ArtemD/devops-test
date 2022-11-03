from fabric import Connection

staging = Connection('root@64.225.70.175')
production = Connection('root@178.128.243.191')

def install_dep_os(c):
    c.run('apt update')
    c.run('apt upgrade -y')
    c.run('apt install python3-pip -y')
    c.run('pip3 install pipenv')

def backup_old_files(c):
    c.run('tar cvpf old.tar *')

def copy_files_to_server(c):
    c.put('latest.tar', remote='/root/')
    c.run('tar xvpf latest.tar')
    c.run('rm latest.tar')

def install_python_libs(c):
    c.run('pipenv install --system')

def run_software(c):
    c.run('uvicorn app:app --host 0.0.0.0 --port 80')

c = staging
install_dep_os(c)
backup_old_files(c)
copy_files_to_server(c)
install_python_libs(c)
run_software(c)

c = production
install_dep_os(c)
backup_old_files(c)
copy_files_to_server(c)
install_python_libs(c)
run_software(c)
