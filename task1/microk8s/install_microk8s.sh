#!/bin/bash

# Install microk8s
sudo snap install microk8s --classic

sudo microk8s status --wait-ready

sudo usermod -a -G microk8s ubuntu
sudo chown -R ubuntu ~/.kube

sudo newgrp microk8s

cd $HOME
mkdir .kube
cd .kube
sudo microk8s config > config

# Alias kubectl to microk8s.kubectl
echo "alias kubectl='microk8s kubectl'" >> ~/.bashrc
source ~/.bashrc

# Print status
microk8s.status
