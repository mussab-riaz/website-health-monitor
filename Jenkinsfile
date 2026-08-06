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
            archiveArtifacts artifacts: 'reports/health_report.csv'
        }

        success {
            emailext(
                subject: "SUCCESS: Website Monitor",
                body: "Website monitor pipeline completed successfully.",
                to: "mussabriaz1368@gmail.com"
            )
        }

        failure {
            emailext(
                subject: "FAILED: Website Monitor",
                body: "Website monitor pipeline failed. Check Jenkins logs.",
                to: "mussabriaz1368@gmail.com"
            )
        }
    }
}