pipeline{
        agent any
        stages{ 
		    stage('---Run Test---'){
                        steps{
                            sh "pytest tests/test_factorials.py"
                        }
                }
        }
}
