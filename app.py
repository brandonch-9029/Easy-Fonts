from flask import Flask, render_template, request, redirect, url_for, send_from_directory

from fontTools import ttLib

import shutil
import os
import modules.generateFormats
import modules.generateCSS

app = Flask(__name__)


# index.html
@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

# load.html
@app.route('/<fileName>/<fontName>/<taskDirectory>/<packageSize>/load', methods=['POST', 'GET'])
def load(fileName ,fontName, taskDirectory, packageSize):
    return render_template('load.html', fileNameJinja=fileName, fontNameJinja=fontName, taskDirectoryJinja=taskDirectory, packageSizeJinja=packageSize)

#formats.html
@app.route('/formats', methods=['GET'])
def formats():
    return render_template('formats.html')

#examples.html
@app.route('/examples', methods=['GET'])
def examples():
    return render_template('formats.html')

# route when Submit button with action="/upload" is clicked
@app.route('/upload', methods=['POST'])
def upload_file():

    # each font package created will have its own task directory
    # looks through task directory to determine next task folder e.g. /tasks/150
    base_directory = "tasks"
    directory_list = [item for item in os.listdir(base_directory) if os.path.isdir(os.path.join(base_directory, item))]
    
    # if task folder is empty, file will be uploaded to /tasks/1
    if len(directory_list) == 0:
        next_task_index = 1
    else:
        directory_list = [int(x) for x in directory_list]
        next_task_index = int(max(directory_list)) + 1

    # saves the uploaded font file into the new task folder
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        new_folder = "tasks/" + str(next_task_index)
        os.mkdir(new_folder)
        font_path = new_folder + "/" + uploaded_file.filename
        uploaded_file.save(font_path)
    
    # detect font metadata
    font = ttLib.TTFont(font_path)
    font_name = font['name'].getDebugName(4)

    #if ttf, convert to woff and woff2
    if uploaded_file.filename.endswith('.ttf'):
        uploaded_file_name = uploaded_file.filename[:-4]
        modules.generateFormats.convertTTF(font_path)

    elif uploaded_file.filename.endswith('.woff'):
        uploaded_file_name = uploaded_file.filename[:-5]
        modules.generateFormats.convertWOFF(font_path)
    
    elif uploaded_file.filename.endswith('.woff2'):
        uploaded_file_name = uploaded_file.filename[:-6]
        modules.generateFormats.convertWOFF2(font_path)

    # create css file for fonts
    modules.generateCSS.generateCSS(font_path, font_name, new_folder)

    # once fonts and css are complete, zip the task directory
    shutil.make_archive(new_folder,'zip', new_folder)
    package_name = new_folder + '.zip'
    # returns package size divided by 1024 to get bytes
    package_size = str(int(os.path.getsize(package_name)/1024))

    return redirect(url_for('load',fileName=uploaded_file_name, fontName=font_name, taskDirectory=next_task_index, packageSize=package_size))

@app.route('/download', methods=['GET'])
def download():

    base_directory = "tasks"
    directory_list = [item for item in os.listdir(base_directory) if os.path.isdir(os.path.join(base_directory, item))]
    directory_list = [int(x) for x in directory_list]
    latest_task = str(int(max(directory_list)))
    
    return send_from_directory('/Easy-Fonts/tasks', latest_task + '.zip')

if __name__ == "__main__":
    app.run(debug=True)