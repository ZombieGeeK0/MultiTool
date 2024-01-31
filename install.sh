sudo su
clear
echo --------------------------------------------------------------------------------------
echo [~] Instalando...
echo --------------------------------------------------------------------------------------
sudo apt-get update
sudo apt-get install python3
sudo apt-get install python3-pip
pip3 install os
pip3 install colarama
pip3 install socket
pip3 install sys
cd..
git clone https://github.com/sherlock-project/sherlock.git
cd sherlock
python3 -m pip install -r requirements.txt
echo --------------------------------------------------------------------------------------------
echo [~] Requerimientos instalados. Usa el comando python3 main.py para inciar MultiTool.
