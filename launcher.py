import subprocess

bash_server = "python telecoweb/manage.py runserver 192.168.1.169:8000"
bash_iot = 'python teleco.py'
commands = [bash_server, bash_iot]

for p in commands:
    process = subprocess.Popen(p.split(), stdout=subprocess.PIPE)
process.wait()