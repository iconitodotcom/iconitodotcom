pipeline {
    agent any

    environment 
    {
        DOCKERHUB_USER = credentials('dockerhub_user')
        DOCKERHUB_TOKEN = credentials('dockerhub_token')
        FLY_API_TOKEN = credentials('fly_api_token')
        VERSION = "JI${env.BUILD_NUMBER}"
        FLY_APP = 'iconitodev-website'
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
                    echo "#### Login to Fly ####"
                    export FLY_API_TOKEN=$FLY_API_TOKEN
                    fly auth token $FLY_API_TOKEN
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
        stage('DEPLOY') {
            steps {
            sh '''
              fly deploy --image $DOCKERHUB_USER/iconitodev:$VERSION --app $FLY_APP --remote-only
            '''
            }
        }
    }
}