pipeline {
    agent any

    environment 
    {
        DOCKERHUB_USER = credentials('dockerhub_user')
        DOCKERHUB_TOKEN = credentials('dockerhub_token')
        VERSION = "JI${env.BUILD_NUMBER}"
    }

    stages {
        stage('PRE_BUILD') {
            steps {
                sh '''
                    echo "#### Verify Dockerfile exist in the proyect repository ####"
                    ls -l Dockerfile
                    echo "#### Verify docker is installed in agent ###"
                    docker --version
                    echo "#### Login to docker hub ###"
                    echo $DOCKERHUB_TOKEN | docker login -u $DOCKERHUB_USER --password-stdin
                '''
            }
        }
        stage('BUILD') {
            steps {
                sh '''
                    docker build -t iconitodev:$VERSION .
                '''
            }
        }
        stage('POST_BUILD') {
            steps {
                sh '''
                    docker tag iconitodev:$VERSION $DOCKERHUB_USER/iconitodev:$VERSION
                    docker push $DOCKERHUB_USER/iconitodev:$VERSION
                '''
            }
        }
    }
}