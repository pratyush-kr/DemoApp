pipeline {
    agent any
    stages {
        // stage('Installing git') {
        //     steps {
        //         sh 'apt install git'
        //     }
        // }
        stage('Checkout') {
            steps {
                sh 'mkdir DemoApp'
                sh 'cd DemoApp'
                sh 'git clone https://github.com/pratyush-kr/DemoApp.git'
            }
        }
        stage('install requirements') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Make Migrations') {
            steps {
                sh 'docker run --rm my-django-app python manage.py makemigrations'
            }
        }
        stage('Migrate') {
            steps {
                sh 'docker run --rm my-django-app python manage.py migrate'
            }
        }
        stage('Run') {
            steps {
                sh 'python3 manage.py runserver'
            }
        }
    }
}
