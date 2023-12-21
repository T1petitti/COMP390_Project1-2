git init
git config user.name "Tyler Petitti"
git config user.email "shawn.petitti.tp@gmail.com"
git add .
echo 'Enter a commit comment:'
read commitComment
git commit -m "$commitComment"
echo 'Enter the remote origin URL:'
read url
git remote add origin "$url"
git branch -M main
git push origin main