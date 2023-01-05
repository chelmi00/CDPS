from subprocess import call
import os

def createEnvironment():
    call(["sudo", "rm", "-r", "practica_creativa2"])
    call(["git", "clone", "https://github.com/CDPS-ETSIT/practica_creativa2.git"])
    call(["sudo", "apt", "update"])
    call(["sudo", "apt", "install", "python3-pip", "-y"])
    call(["pip3", "install", "-r", "practica_creativa2/bookinfo/src/productpage/requirements.txt"])
    call(['pip', 'install', '--force-reinstall', '-v', "urllib3==1.21.1"])
    call(['pip', 'install', '--force-reinstall', '-v', "chardet==3.0.2"])
    os.environ['GROUP_NUMBER']="20"

def modifyHTML():
    html=open("practica_creativa2/bookinfo/src/productpage/templates/productpage.html", "r")
    aux=open("practica_creativa2/bookinfo/src/productpage/templates/auxiliar.html", "w+")
    for line in html:
        if "{% block title %}Simple Bookstore App{% endblock %}" in line:
            aux.write("{% block title %}" + str(os.environ.get('GROUP_NUMBER')) + "{% endblock %}")
        else:
            aux.write(line)
    call(["mv", "practica_creativa2/bookinfo/src/productpage/templates/auxiliar.html", "practica_creativa2/bookinfo/src/productpage/templates/productpage.html"])
    html.close()
    aux.close()

def main():
    # createEnvironment()
    modifyHTML()
    # call(["python3", "practica_creativa2/bookinfo/src/productpage/productpage_monolith.py", "2001"])

if __name__=="__main__":
    main()
