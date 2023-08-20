import os
import shutil

while True:
    try:
        folder_path = input('Enter the path :   ')
        os.chdir(folder_path)

        vedio = (".3gp", ".avi", ".flv", ".mkv", ".mp4", ".mpeg", ".mov", ".qt", ".rm", ".svi", ".wmv" )
        audio=(".aac", ".aiff", ".amr", ".ape", ".flac", ".m4a", ".mp3", ".ogg", ".wav", ".wma")
        image=(".jpeg", ".png", ".gif", ".tiff", ".raw", ".webp", ".ico", ".bmp", ".psd", ".ai")   
        book = (".azw", ".azw3", ".cbz", ".cbr", ".epub", ".fb2", ".html", ".mobi", ".pdf", ".prc", ".txt")
        compressed=(".7z", ".ace", ".arj", ".bz2", ".cab", ".cpio", ".gzip", ".lzh", ".lzma", ".rar", ".rpm", ".tar", ".tgz", ".zip")
        app=(".apk", ".ipa", ".bar", ".exe", ".nxa", ".pkg", ".xblig", ".uwp")
        
        for file in os.listdir():
            if file.endswith(vedio):
                new_folder = "vedios Files"
                if not os.path.exists(new_folder):
                    os.makedirs(new_folder)
                shutil.move(file, os.path.join(new_folder, file))

            elif file.endswith(audio):
                    new_folder = "audios Files"
                    if not os.path.exists(new_folder):
                        os.makedirs(new_folder)
                    shutil.move(file, os.path.join(new_folder, file))

            elif file.endswith(image):
                    new_folder = "images Files"
                    if not os.path.exists(new_folder):
                        os.makedirs(new_folder)
                    shutil.move(file, os.path.join(new_folder, file))

            elif file.endswith(book):
                    new_folder = "books Files"
                    if not os.path.exists(new_folder):
                        os.makedirs(new_folder)
                    shutil.move(file, os.path.join(new_folder, file))

            elif file.endswith(compressed):
                    new_folder = "compressed Files"
                    if not os.path.exists(new_folder):
                        os.makedirs(new_folder)
                    shutil.move(file, os.path.join(new_folder, file))

            elif file.endswith(app):
                    new_folder = "app Files"
                    if not os.path.exists(new_folder):
                        os.makedirs(new_folder)
                    shutil.move(file, os.path.join(new_folder, file))
        
    except:
        print ('error')