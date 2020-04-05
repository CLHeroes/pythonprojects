pipeline {
    agent any
    stages {
        stage("Create important files!") {
            steps {
                sh """
                    touch importantfile1
                    touch importantfile2
                    touch importantfile3
                """
            } //steps 
        } //stage
        stage("Run helloworld") {
            steps {
                sh """
                    python helloworld.py
                """
            } //steps
        } //stage
        stage("Run conditionals.py") {
            steps {
                sh """
                    python conditionals.py
                """
            } //steps
        } //stage
    } //stages
    post {
        always {
            sh """
                rm -f importantfile1
                rm -f importantfile2
                rm -f importantfile3
            """
        }
    }
} //pipeline