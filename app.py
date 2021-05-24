from predict import predict, plot_schema
import requests
from flask import Flask, render_template, Response,request, redirect, url_for,flash,jsonify
import os
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
app = Flask(__name__)
import urllib.request
urllib.request.urlretrieve('https://ml.azure.com/fileexplorerAzNB?wsid=/subscriptions/cb22c59f-24c2-4398-b363-f2e4948b004f/resourcegroups/beasiback_test/workspaces/adn&tid=8c645637-2ab2-41e5-b76a-68592e20eebb&activeFilePath=Users/diamad/PROJET%20DEEPL/model.h5', 'model.h5')
UPLOAD_FOLDER = 'static/uploads/'
 
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.errorhandler(404)
def not_found(error):
  resp = jsonify( { 
    u'status': 404, 
    u'message': u'Resource not found' 
  } )
  resp.status_code = 404
  return resp

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict/api',methods=['POST'])
def predict_image(image_path):
    if request.method == 'POST':
        file_url = request.json['url']
        lang = request.json['languages'] or 'fra'
        filename = os.path.basename(file_url or "")
        if file_url and allowed_file(filename):
            resp = jsonify({u'message': u'Hello'})
        else:
            resp = jsonify( {
                u'status': 415,
                u'message': u'Unsupported Media Type' 
            } )
            resp.status_code = 415
            return resp
    else:
        resp = jsonify( {
        u'status': 405, 
        u'message': u'The method is not allowed for the requested URL' 
        } )
        resp.status_code = 405
        return resp


@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename('retina_image.jpg')
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        return render_template('index.html', filename=filename)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
 
@app.route('/display/<filename>')
def display_image(filename):
    pred = predict('./static/uploads/' + filename)
    plot_url = plot_schema(pred['prediction'], pred['predicted_label'])
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == '__main__':
  app.run(debug=True)