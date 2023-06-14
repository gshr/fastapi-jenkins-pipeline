pipeline {
    agent any

    stages {
        // stage('Clone Code') {
        //     steps {
        //         git 'https://github.com/gshr/hello-world-fastapi.git'
        //     }
        // }
        
        stage('Check') {
            steps {
                sh 'ls -l'
            }
        }
        
        stage('Build and Deploy') {
            steps {
                sh "sudo docker build -t fastapi ."
                script {
                try {
                    sh "sudo docker kill fastapi"
                    sh "sudo docker remove fastapi"
                    sh "sudo docker  run --name fastapi -d -p 80:80 fastapi"
                }
                catch (Exception e){
                    echo "No image to kill  "
                    sh "sudo docker  run --name fastapi -d -p 80:80 fastapi"
                    
                }
                }
            }
           
            }
        }
    }

