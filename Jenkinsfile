pipeline {
    agent any

    environment {
        SONARQUBE_ENV = 'SonarQube'
    }

    tools {
        // This name must EXACTLY match what you named it in
        // Manage Jenkins -> Tools -> SonarQube Scanner installations
        'hudson.plugins.sonar.SonarRunnerInstallation' 'sonar-scanner'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/arokiyasamypreethi-netizen/sonarqube_jenkins-project.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv("${SONARQUBE_ENV}") {
                    sh "${tool 'sonar-scanner'}/bin/sonar-scanner"
                }
            }
        }

        stage('Quality Gate') {
            steps {
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
