pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-u root'
        }
    }

    stages {
        stage('Install Requirements') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Syntax Check') {
            steps {
                sh 'python -m py_compile app/*.py'
            }
        }

        stage('Run App (Test)') {
            steps {
                // Create a temporary runner script
                sh '''
                echo "
from app import create_app
app = create_app()
app.run(host='0.0.0.0', port=5000)
                " > run_app.py
                '''

                // Run it in background
                sh 'nohup python run_app.py &'
                sh 'sleep 5'
                sh 'curl http://localhost:5000 || true'
                sh 'curl http://localhost:5000/ping || true'
                sh 'curl http://localhost:5000/version || true'
            }
        }
    }

    post {
        always {
            sh 'pkill -f run_app.py || true'
        }
    }
}

