# app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from photos import photos

app = Flask(__name__)
CORS(app)

# Get all photos
@app.route('/photos', methods=['GET'])
def get_photos():
    return jsonify(photos)

# Get a specific photo by ID
@app.route('/photos/<int:photo_id>', methods=['GET'])
def get_photo(photo_id):
    photo = [photo for photo in photos if photo['id'] == photo_id]
    if len(photo) == 0:
        return jsonify({'error': 'Photo not found'})
    return jsonify(photo[0])

# Upload a new photo
@app.route('/photos', methods=['POST'])
def upload_photo():
    new_photo = {
        'id': photos[-1]['id'] + 1,
        'title': request.json['title'],
        'url': request.json['url'],
        'tags': request.json['tags']
    }
    photos.append(new_photo)
    return jsonify({'message': 'Photo uploaded successfully'})

# Update an existing photo
@app.route('/photos/<int:photo_id>', methods=['PUT'])
def update_photo(photo_id):
    photo = [photo for photo in photos if photo['id'] == photo_id]
    if len(photo) == 0:
        return jsonify({'error': 'Photo not found'})
    photo[0]['title'] = request.json['title']
    photo[0]['url'] = request.json['url']
    photo[0]['tags'] = request.json['tags']
    return jsonify({'message': 'Photo updated successfully'})

# Delete a photo
@app.route('/photos/<int:photo_id>', methods=['DELETE'])
def delete_photo(photo_id):
    photo = [photo for photo in photos if photo['id'] == photo_id]
    if len(photo) == 0:
        return jsonify({'error': 'Photo not found'})
    photos.remove(photo[0])
    return jsonify({'message': 'Photo deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)

# photos.py (Data for testing)
photos = [
    {
        'id': 1,
        'title': 'Sunset at the Beach',
        'url': 'https://example.com/photo1.jpg',
        'tags': ['sunset', 'beach', 'nature']
    },
    {
        'id': 2,
        'title': 'Mountain Landscape',
        'url': 'https://example.com/photo2.jpg',
        'tags': ['mountain', 'landscape', 'nature']
    }
]
