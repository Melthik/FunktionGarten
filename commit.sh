python3 process.py main.tex
pelican content -s publishconf.py -o docs
git add *
git commit -m "Updates"
git push --set-upstream origin main
