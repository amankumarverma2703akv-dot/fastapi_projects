git init

cat <<EOT > .gitignore
__pycache__/
*.pyc
*.pyo
*.pyd
*.db
.env
*.joblib
models/
.ipynb_checkpoints/
EOT

git add .
git commit -m "Initial commit: BFSI Loan FastAPI project structure"
git branch -M main
git remote add origin https://github.com/amankumarverma2703akv-dot/bfsi_project.git
git push -u origin main