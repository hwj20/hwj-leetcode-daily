@echo off
SET datestamp=%DATE:~-10%
echo Adding all changes to git...
git add .
echo Committing with the date as message...
git commit -m "Commit on %datestamp%"
echo Pushing to remote repository...
git push
echo Done.
pause
