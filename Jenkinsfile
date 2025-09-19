pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/oumaymamansri/JenkinsP.git'
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings -q'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t calculator-app .'
            }
        }
        stage('Run App') {
            steps {
                sh 'docker run -it --rm calculator-app'
            }
        }
    }
}
