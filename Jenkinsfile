pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking source code'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image'

                bat 'docker build -t devops-monitoring-app:1.0 .'
            }
        }

        stage('Test Application') {
            steps {
                echo 'Testing application'

                bat 'docker run --rm devops-monitoring-app:1.0 python -c "import app; print(app.health())"'
            }
        }
    }

    post {
        success {
            echo 'CI Pipeline completed successfully!'
        }

        failure {
            echo 'CI Pipeline failed. Check console output.'
        }
    }
}