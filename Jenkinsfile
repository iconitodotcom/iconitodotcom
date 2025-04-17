pipeline {
    agent any

    stages {
        stage('PRE_BUILD') {
            steps {
                sh 'ls -la'
            }
        }
        stage('BUILD') {
            steps {
                sh 'docker --version'
            }
        }
        stage('POST_BUILD') {
            steps {
                echo 'Hello World'
            }
        }
    }
}