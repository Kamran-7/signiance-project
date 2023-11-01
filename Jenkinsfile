pipeline {
    agent any
    environment {
        GITHUB_TOKEN = credentials('ghcr-pat')
        IMAGE_NAME = 'kamran-7/python-app' 
    }
    stages {
        stage("Clone Code") {
            steps {
                git branch: 'main', credentialsId: 'github-pat', url: 'https://github.com/Kamran-7/signiance-project.git'
            }
        }
        stage('Build docker image') {
            steps {
                dir('/var/lib/jenkins/workspace/signiance-project') {
                    script {
                        def lastBuildNumber = env.BUILD_NUMBER.toInteger() - 1
                        def newVersion = "1.0.${lastBuildNumber}"

                        // Set the updated version as the IMAGE_VERSION
                        env.IMAGE_VERSION = newVersion

                        // Build the Docker image with the updated version
                       // sh "docker rmi --force $(docker images -q)"
                        sh "docker system prune -a --volumes --force"
                        sh "docker build -t $IMAGE_NAME:$env.IMAGE_VERSION ."
                    }
                }
            }
        }
        stage('Login to GHCR') {
            steps {
                sh 'echo $GITHUB_TOKEN_PSW | docker login ghcr.io -u $GITHUB_TOKEN_USR --password-stdin'
            }
        }
        stage('Tag docker image') {
            steps {
                sh "docker tag $IMAGE_NAME:$env.IMAGE_VERSION ghcr.io/$IMAGE_NAME:$env.IMAGE_VERSION"
            }
        }
        stage('Push image') {
            steps {
                sh "docker push ghcr.io/$IMAGE_NAME:$env.IMAGE_VERSION"
            }
        }
        stage('Deploy') {
            steps {
                // sh "docker stop python-app"
                // sh "docker rm python-app"
                sh "docker run --name python-app -d -p 5000:80 ghcr.io/$IMAGE_NAME:$env.IMAGE_VERSION"
            }
        }  
    }
    post {
      always {
          sh 'docker logout ghcr.io'
        }
    }
}
