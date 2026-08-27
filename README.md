# Jenkins + SonarQube Sample Pipeline

Minimal repo to test a Jenkins pipeline that runs a SonarQube scan on a GitHub-hosted project.

## Files
- `Jenkinsfile` — the pipeline definition Jenkins will run.
- `sonar-project.properties` — tells the SonarQube scanner what to analyze.
- `app.py` — sample source file with a few intentional code smells (unused import, hardcoded password, unused variable) so you get visible results on the SonarQube dashboard.
- `test_app.py` — a small unit test file, just to make the repo look realistic.

## Before you push to GitHub
1. Push all 5 files to the root of a new GitHub repo.
2. In `Jenkinsfile`, replace the `git url` with your actual repo URL.

## Jenkins one-time setup
1. **Manage Jenkins → Tools** — add a SonarQube Scanner installation (give it any name, e.g. `sonar-scanner`).
2. **Manage Jenkins → System → SonarQube servers** — add your SonarQube server, name it exactly `SonarQube` (or change `SONARQUBE_ENV` in the Jenkinsfile to match whatever you name it), and paste in a token generated from SonarQube (My Account → Security → Generate Token).
3. **SonarQube → Administration → Webhooks** — add a webhook pointing to `http://<your-jenkins-url>/sonarqube-webhook/` so the Quality Gate stage can get its result back.
4. Create a new Pipeline job in Jenkins, point it at your GitHub repo, and set it to use the `Jenkinsfile` from SCM.
