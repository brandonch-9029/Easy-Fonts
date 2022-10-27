from flask import Flask, render_template, request, redirect, url_for

import os

app = Flask(__name__)


# index.html
@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


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
        next_task_index = int(max(directory_list)) + 1

    # saves the uploaded font file into the new task folder
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        new_folder = "tasks/" + str(next_task_index)
        os.mkdir(new_folder)
        uploaded_file.save(new_folder + "/" + uploaded_file.filename)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)