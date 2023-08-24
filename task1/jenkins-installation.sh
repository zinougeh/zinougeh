#!/bin/bash

# Check if Jenkins is already installed
if sudo systemctl is-active --quiet jenkins; then
    echo "Jenkins is already installed and running."
    exit 0
fi

# Update and upgrade the package repositories
sudo yum update -y   # For Amazon Linux

sudo wget -O /etc/yum.repos.d/jenkins.repo \
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key \
    https://pkg.jenkins.io/redhat-stable/jenkins.repo
sudo yum upgrade
sudo amazon-linux-extras install java-openjdk11 -y

sudo yum install jenkins -y
# Start Jenkins service
sudo systemctl enable jenkins

sudo systemctl start jenkins

# Display the initial Jenkins admin password
echo "Jenkins initial admin password:"
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
