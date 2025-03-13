pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git credentialsId: '71901886-3673-4bb3-a4a0-dcdacad0d7ea', branch: 'main', url: 'https://github.com/suting777/selenium-jenkins-test.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Selenium Test') {
            steps {
                sh 'python test_selenium.py'
            }
        }
    }
}
 
