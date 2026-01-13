import os
import requests
import json
from flask import Flask, render_template, request, jsonify, send_file
from werkzeug.utils import secure_filename
import anthropic
from pathlib import Path

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB max
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'videos'

# Create necessary folders
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

def allowed_file(filename):
      return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class AIVideoBot:
      def __init__(self):
                self.client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
                self.runway_api_key = os.getenv('RUNWAY_API_KEY')
                self.synthesia_api_key = os.getenv('SYNTHESIA_API_KEY')

      def generate_ad_script(self, product_name, product_description, key_features):
                """Generate marketing script using Claude"""
                prompt = f"""Create a compelling 30-second product ad script for:
        Product: {product_name}
        Description: {product_description}
        Key Features: {key_features}

        Format the response as:
        SCRIPT: [engaging 30-second ad script]
        VOICEOVER: [voiceover text, natural and persuasive]
        MUSIC_MOOD: [suggested background music style]
        PACING: [slow/medium/fast]"""

          message = self.client.messages.create(
                        model="claude-3-5-sonnet-20241022",
                        max_tokens=1024,
                        messages=[{"role": "user", "content": prompt}]
          )
        return message.content[0].text

    def create_video_with_runway(self, image_path, script, video_style="cinematic"):
              """Generate video using Runway AI"""
              try:
                            with open(image_path, 'rb') as f:
                                              files = {'image': f}
                                              headers = {'Authorization': f'Bearer {self.runway_api_key}'}

                data = {
                                      'prompt': script,
                                      'style': video_style,
                                      'duration': 30,
                                      'quality': 'high'
                }

                response = requests.post(
                                      'https://api.runwayml.com/v1/video_generation',
                                      files=files,
                                      data=data,
                                      headers=headers
                )

                if response.status_code == 200:
                                      return response.json().get('video_url')
else:
                    return None
except Exception as e:
            print(f"Runway API error: {e}")
            return None

    def create_video_with_synthesia(self, image_path, voiceover_text):
              """Generate video using Synthesia (avatar-based)"""
        try:
                      with open(image_path, 'rb') as f:
                                        image_data = f.read()
                                        headers = {'Authorization': f'Bearer {self.synthesia_api_key}'}

                payload = {
                                      'video': {
                                                                'personsArray': [
                                                                                              {
                                                                                                                                'background': {
                                                                                                                                                                      'type': 'image',
                                                                                                                                                                      'url': image_path
                                                                                                                                  }
                                                                                                }
                                                                ],
                                                                'scriptText': voiceover_text,
                                                                'fps': 24,
                                                                'quality': 'high'
                                      }
                }

                response = requests.post(
                                      'https://api.synthesia.io/v2/videos',
                                      json=payload,
                                      headers=headers
                )

                if response.status_code == 201:
                                      return response.json().get('id')
else:
                    return None
except Exception as e:
            print(f"Synthesia API error: {e}")
            return None

bot = AIVideoBot()

@app.route('/')
def index():
      return render_template('index.html')

@app.route('/api/upload', methods=['POST'])
def upload_file():
      if 'file' not in request.files:
                return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if file.filename == '':
              return jsonify({'error': 'No file selected'}), 400

    if not allowed_file(file.filename):
              return jsonify({'error': 'Invalid file type'}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    return jsonify({
              'success': True,
              'filename': filename,
              'filepath': filepath
    })

@app.route('/api/generate-script', methods=['POST'])
def generate_script():
      data = request.json
    product_name = data.get('productName')
    product_description = data.get('productDescription')
    key_features = data.get('keyFeatures')

    if not all([product_name, product_description, key_features]):
              return jsonify({'error': 'Missing required fields'}), 400

    try:
              script = bot.generate_ad_script(product_name, product_description, key_features)
        return jsonify({'script': script})
except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/generate-video', methods=['POST'])
def generate_video():
      data = request.json
    image_filename = data.get('imageFilename')
    script = data.get('script')
    video_style = data.get('videoStyle', 'cinematic')
    api_choice = data.get('apiChoice', 'runway')

    if not image_filename or not script:
              return jsonify({'error': 'Missing image or script'}), 400

    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)

    if not os.path.exists(image_path):
              return jsonify({'error': 'Image not found'}), 404

    try:
              if api_choice == 'runway':
                            video_url = bot.create_video_with_runway(image_path, script, video_style)
else:
            video_url = bot.create_video_with_synthesia(image_path, script)

        if video_url:
                      return jsonify({
                                        'success': True,
                                        'videoUrl': video_url,
                                        'status': 'Video generated successfully'
                      })
else:
            return jsonify({'error': 'Failed to generate video'}), 500
except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0', port=5000)
