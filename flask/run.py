from app import create_app
import os

extra_dirs = ['app',]
extra_files = extra_dirs[:]
for extra_dir in extra_dirs:
    for dirname, dirs, files in os.walk(extra_dir):
        for filename in files:
            filename = os.path.join(dirname, filename)
            if os.path.isfile(filename):
                extra_files.append(filename)

if __name__ == '__main__':
    app = create_app('development')
    app.run(extra_files=extra_files)