stage('Test Application') {
    steps {
        echo 'Testing application'

        bat 'docker run --rm devops-monitoring-app:1.0 python -c "from app import app; r=app.test_client().get(\'/health\'); assert r.status_code == 200; assert r.get_json()[\'status\'] == \'healthy\'; print(\'Health check passed\')"'
    }
}