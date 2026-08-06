pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Getting code from GitHub'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Monitor') {
            steps {
                sh 'python3 monitor.py'
            }
        }
    }

    post {

        always {
            archiveArtifacts artifacts: 'reports/health_report.csv', fingerprint: true
        }

        success {
            echo 'Build completed successfully ✅'
        }

        failure {
            echo 'Build failed ❌'
        }
    }
}