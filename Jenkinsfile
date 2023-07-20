pipeline {
    agent any
    stages {
        stage('Removing old') {
            steps {
                sh 'rm -rf DemoApp'
            }
        }
        stage('Checkout') {
            steps {
                sh 'mkdir DemoApp'
                sh 'cd DemoApp'
                sh 'git clone https://github.com/pratyush-kr/DemoApp.git'
            }
        }
        stage('Docker build') {
            steps {
                sh 'snap install docker'
                sh 'docker build -t DempApp .'
            }
        }
    }
}

