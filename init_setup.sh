echo [$(date)]: "START"

echo [$(date)]: "Creating env with python 3.8 version"

conda create --prefix ./ml_env_1 python=3.8 -y

echo [$(date)]: "Activating the environment"

source activate ./ml_env_1

echo [$(date)]: "Installing the dev requirements"

pip install -r requirements.txt

echo [$(date)]: "END"