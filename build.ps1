$ver = $args[0]
python -m PyInstaller --noconfirm --onedir --windowed --name "Game" --add-data "maps;maps/" --add-data "BAHNSCHRIFT.TTF;."  "main.py"
Compress-Archive "dist/Game/*" "dist.zip" -Force
git add -A
git commit -am "auto commit"
git push
gh release create $ver 'dist.zip#Windows (Windows only for now)' --title $ver -n " "