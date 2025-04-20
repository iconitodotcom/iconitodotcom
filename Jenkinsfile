pipeline {
    agent any

    environment 
    {
        DOCKERHUB_USER = credentials('dockerhub_user')
        DOCKERHUB_TOKEN = credentials('dockerhub_token')
        IMAGE_NAME = "iconitodev"
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
                sh 'docker build -t $IMAGE_NAME:$VERSION .'
            }
        }
        stage('POST_BUILD') {
            steps {
                sh '''
                    docker tag $IMAGE_NAME:$VERSION $DOCKERHUB_USER/$IMAGE_NAME:$VERSION
                    docker push $DOCKERHUB_USER/$IMAGE_NAME:$VERSION
                '''
            }
        }
    }
}