pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-username/your-repo.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t my-django-app .'
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
    }
}
