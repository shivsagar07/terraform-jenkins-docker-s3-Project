
# Jenkinsfile
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-username/devops-s3-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t s3-backend-app .'
            }
        }

        stage('Run Application') {
            steps {
                sh 'docker run s3-backend-app'
            }
        }
    }
}
