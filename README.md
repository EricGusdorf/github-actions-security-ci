# GitHub Actions CI/CD with Security Scanning

Sample Python project configured with GitHub Actions (`security-ci.yml`) to run `pytest`, `safety check`, and `bandit -r src/ -ll`.

## Part 1: Initial Push (Vulnerable Dependencies)
`requirements.txt` starts with the assignment's vulnerable versions:
- `pytest==7.4.0`
- `requests==2.20.0`
- `urllib3==1.24.1`

## Part 3: Remediated Dependencies
Copy `requirements-fixed.txt` over `requirements.txt`, then commit and push:
```bash
cp requirements-fixed.txt requirements.txt
git add requirements.txt
git commit -m "fix(deps): upgrade requests to 2.32.4 and urllib3 to 2.5.0 to resolve known CVEs"
git push origin main
```
