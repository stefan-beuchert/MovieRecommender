pipeline {
    agent any
    stages {
        stage('build') {
        steps {
            echo 'building'
            sh 'pip install pybuilder'
            sh 'pyb'
            }
        }
    }
}