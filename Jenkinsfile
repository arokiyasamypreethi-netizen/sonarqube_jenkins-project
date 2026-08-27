pipeline {
    agent any

    environment {
        // This name must EXACTLY match the SonarQube server name you configure
        // in Jenkins -> Manage Jenkins -> System -> SonarQube servers
        SONARQUBE_ENV = 'SonarQube'
    }

    stages {

        stage('Checkout') {
            steps {
                // Replace with your own GitHub repo URL
                git branch: 'main', url: 'https://github.com/arokiyasamypreethi-netizen/sonarqube_jenkins-project.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                // 'sonar-scanner' below must match the name you gave the
                // SonarQube Scanner tool in Jenkins -> Manage Jenkins -> Tools
                withSonarQubeEnv("${SONARQUBE_ENV}") {
                    sh 'sonar-scanner'
                }
            }
        }

        stage('Quality Gate') {
            steps {
                // Pauses the pipeline until SonarQube sends back the analysis result
                // Requires a webhook configured in SonarQube pointing to Jenkins
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully! Check the SonarQube dashboard for results.'
        }
        failure {
            echo '❌ Pipeline failed. Check the console output above for details.'
        }
    }
}
