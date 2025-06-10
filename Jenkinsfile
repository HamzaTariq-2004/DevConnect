pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-u root' // optional: run as root for installing packages if needed
        }
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
            }
        }

        stage('Run App (Test)') {
            steps {
                sh 'nohup python app.py &'
                sh 'sleep 5' // wait a bit for app to run
                sh 'curl http://localhost:5000 || true'
            }
        }
    }

    post {
        always {
            sh 'pkill -f app.py || true'
        }
    }
}

