# build docker image from DockerfileServer
# Rasa Server with spellchicking python package
sudo docker build --tag rasa_custom:2.0 . -f DockerfileRasa

# train and store model
sudo docker run --user 1002 -it -v $(pwd):/app rasa_custom:2.0 train --domain domain.yml --data data --out models --config configs/config_spacy.yml --augmentation 20

# build docker image from DockerfileAction
# Rasa Action Server 
sudo docker build --tag rasa_action:2.0 . -f DockerfileAction

# serve images via docker-compose
sudo docker-compose up -d
