node('large') {
    currentBuild.result = "SUCCESS"
    try {
        stage('Checkout'){
            checkout scm
        }
        stage('CI-Test'){
            sh """
            source /home/jenkins/venv/molecule/bin/activate
            cd nginx-proxy-role
            molecule test
            """
        }
    }
    catch (err) {
        currentBuild.result = "FAILURE"
        throw err
    }
}