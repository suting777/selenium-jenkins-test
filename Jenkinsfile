pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git credentialsId: '71901886-3673-4bb3-a4a0-dcdacad0d7ea', branch: 'main', url: 'https://github.com/suting777/selenium-jenkins-test.git'
            }
        }

        stage('Setup Environment') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat 'pytest --junitxml=report.xml --html=report.html --self-contained-html'
            }
        }

        stage('Publish Report') {
            steps {
                script {
                    publishHTML(target: [
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: '.',
                        reportFiles: 'report.html',
                        reportName: 'Test Report'
                    ])
                }
            }
        }
    }
}
