sudo apt-get update
sudo apt-get install python3

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py --user

pip install pygame --user

python3 main.py
