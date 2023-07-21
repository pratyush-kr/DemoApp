pipeline {
    
    agent any
    triggers {  
        githubPush()  
    }  
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
                docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials')
                sh 'docker build -t DemoApp .'
            }
        }
    }
}

