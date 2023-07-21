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
                sh 'docker build -t demo-app .'
            }
        }
        stage('Docker deploy') {
            steps {
                sh 'docker run -d -p 8000:8000 demo-app'
            }
        }
    }
}

