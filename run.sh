ENV="/env"
ENV_DIR=$(pwd)$ENV
if [ ! -d $ENV_DIR ]; then
       python3 -m venv env
       source env/bin/activate
else
	source env/bin/activate
fi

pip3 install -r requirements.txt
python3 main.py
