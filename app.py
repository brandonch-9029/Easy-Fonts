from flask import Flask, render_template, request, redirect, url_for

from fontTools import ttLib

import os
import modules.generateFormats

app = Flask(__name__)


# index.html
@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

# load.html
@app.route('/<fileName>/<fontName>/<taskDirectory>/load', methods=['POST', 'GET'])
def load(fileName ,fontName, taskDirectory):
    return render_template('load.html', fileNameJinja=fileName, fontNameJinja=fontName, taskDirectoryJinja=taskDirectory)

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
        modules.generateFormats.convertTTF(font_path,new_folder)

    elif uploaded_file.filename.endswith('.woff'):
        uploaded_file_name = uploaded_file.filename[:-4]
    
    elif uploaded_file.filename.endswith('.woff2'):
        uploaded_file_name = uploaded_file.filename[:-5]

    return redirect(url_for('load',fileName=uploaded_file_name, fontName=font_name, taskDirectory=next_task_index))

if __name__ == "__main__":
    app.run(debug=True)