ren *.jpg x.*
ren *.webp x.*
ren *.png x.*
ffmpeg -i x.jpg -vf scale=256:256 img.jpg && del x.jpg
ffmpeg -i x.webp -vf scale=256:256 img.jpg && del x.webp
ffmpeg -i x.png -vf scale=256:256 img.jpg && del x.png
python -m folderikon