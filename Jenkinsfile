
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
                echo 'Testing Flask health endpoint'

                bat '''
                docker run --rm devops-monitoring-app:1.0 python -c "from app import app; r=app.test_client().get('/health'); assert r.status_code == 200; assert r.get_json()['status'] == 'healthy'; print('Health check passed')"
                '''
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
