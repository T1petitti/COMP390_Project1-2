#pytest -v
#pytest_status=$?
#pytest_pass=0
#if [ $pytest_status -eq $pytest_pass ]
#then
  git add .
  echo "Enter a commit message: "
  read commitComment
  git commit -m "$commitComment"
  echo "what branch should the commit be pushed to?"
  read branch
  git push origin "$branch"
#else
#  echo Unit tests did not pass - modify tests to PASS before creating/pushing a commit
#fi