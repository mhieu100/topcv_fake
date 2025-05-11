from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Create uploads directory if it doesn't exist
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():  
    print(request.files)
    # Check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    
    file = request.files['file']
    
    # If user does not select file, browser also
    # submits an empty file without filename
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file:
        # Save the file to the uploads folder
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return jsonify({
            'message': 'File uploaded successfully',
            'filename': file.filename,
            'path': filepath
        }), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 