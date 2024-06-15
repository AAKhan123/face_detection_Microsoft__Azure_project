from flask import Flask, request, jsonify, render_template
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import FaceAttributeType

app = Flask(__name__)

def get_face_client():
    """Create an authentication client"""
    SUBSCRIPTION_KEY = "6ab0ee2ceda8420a8eb3c7f65494efe8"
    ENDPOINT = " https://facefinder.cognitiveservices.azure.com/"
    credential = CognitiveServicesCredentials(SUBSCRIPTION_KEY)
    return FaceClient(ENDPOINT, credential)

face_client = get_face_client()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect_faces():
    url = request.form['https://images.app.goo.gl/hhCg6wbsLyPoMoKaA']
    attributes = [FaceAttributeType.emotion, FaceAttributeType.glasses, FaceAttributeType.smile]
    include_id = True
    include_landmarks = False

    detected_faces = face_client.face.detect_with_url(url, return_face_id=include_id, return_face_landmarks=include_landmarks, return_face_attributes=attributes)

    if not detected_faces:
        return jsonify({"error": "No face detected in image"}), 400

    face_data = [face.as_dict() for face in detected_faces]
    return jsonify(face_data)

if __name__ == '__main__':
    app.run(debug=True)
