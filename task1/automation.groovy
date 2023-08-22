pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the repository
                checkout scm
            }
        }

        stage('Install Terraform') {
            steps {
                // Install Terraform
                sh 'curl -O https://releases.hashicorp.com/terraform/0.15.5/terraform_0.15.5_linux_amd64.zip'
                sh 'unzip terraform_0.15.5_linux_amd64.zip'
                sh 'sudo mv terraform /usr/local/bin/'
                sh 'rm terraform_0.15.5_linux_amd64.zip'
            }
        }

        stage('Terraform Apply') {
            steps {
                // Run Terraform commands
                sh 'terraform init'
                sh 'terraform apply -auto-approve'
            }
        }
    }
}
