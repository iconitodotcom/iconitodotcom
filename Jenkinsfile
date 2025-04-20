pipeline {
    agent any

    environment 
    {
        DOCKERHUB_USER = credentials('dockerhub_user')
        DOCKERHUB_TOKEN = credentials('dockerhub_token')
    }

    stages {
        stage('PRE_BUILD') {
            steps {
                sh '''
                    echo "#### Verify Dockerfile exist in the proyect repository ####"
                    ls -l Dockerfile
                    echo "#### Verify docker is installed in agent ###
                    docker --version
                    echo "#### Login to docker hub ###
                    echo $DOCKERHUB_USER | docker login -u $DOCKERHUB_TOKEN --password-stdin
                '''
            }
        }
        stage('BUILD') {
            steps {
                sh 'Building image'
            }
        }
        stage('POST_BUILD') {
            steps {
                echo 'Push image to docker hub'
            }
        }
    }
}