// Jenkinsfile
pipeline {
    // 1. Agent: Specifies where the pipeline will run. 'any' means any available Jenkins agent.
    agent any

    // 2. Stages: The main body of the pipeline, divided into logical steps.
    stages {

        // Stage 1: Checkout Code
        stage('Checkout') {
            steps {
                echo 'Checking out the code from GitHub...'
                // 'checkout scm' is a special step that fetches the source code
                // from the repository linked to this Jenkins job.
                checkout scm
            }
        }

        // Stage 2: Install Dependencies
        stage('Install Dependencies') {
            steps {
                echo 'Setting up a Python virtual environment and installing packages...'
                // It's a best practice to use a virtual environment to keep dependencies
                // isolated from the main system.
                sh 'python3 -m venv venv'
                // The 'sh' step executes a shell command.
                // We activate the virtual environment and then use pip to install
                // the libraries listed in our requirements.txt file.
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        // Stage 3: Run Tests
        stage('Run Tests') {
            steps {
                echo 'Running unit tests with pytest...'
                // Here, we activate the virtual environment again and run pytest.
                // If any test fails, pytest will exit with an error, and Jenkins
                // will automatically fail this stage and stop the pipeline.
                sh '. venv/bin/activate && pytest'
            }
        }
    }

    // 3. Post-Actions: These actions run after all the stages are complete.
    post {
        // 'always' means this will run regardless of whether the pipeline
        // succeeded or failed. It's perfect for cleanup tasks.
        always {
            echo 'Cleaning up the workspace...'
            // 'deleteDir()' is a Jenkins step to delete the current directory's contents,
            // which includes the virtual environment and checked-out code.
            deleteDir()
        }
    }
}

