pipeline {
    agent {
        docker {
            image 'roemer/universal-jenkins-agent:latest'
        }
    }

    environment {
        PIP_NO_CACHE_DIR = 'off'
        PYTHONUNBUFFERED = '1'
    }

    stages {
        stage('Install Flask') {
            steps {
                sh 'pip install flask'
            }
        }

        stage('Syntax Check') {
            steps {
                sh 'python -m py_compile app.py'
                sh 'python -m py_compile routes.py'
            }
        }

        stage('Run App (Test)') {
            steps {
                sh 'python app.py & sleep 5'
                sh 'curl -f http://localhost:5000/ping'
                sh 'curl -f http://localhost:5000/contact || true'
                sh 'curl -f http://localhost:5000/about || true'
                sh 'curl -f http://localhost:5000/version || true'
            }
        }
    }

    post {
        always {
            sh 'pkill -f app.py || true'
        }
    }
}
