import os
import logging
import re
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key-change-in-production')
app.config['DEBUG'] = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'

# Security headers
@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

def validate_name(name):
    """Validate and sanitize the name parameter"""
    if not name:
        return None
    
    # Remove potentially harmful characters
    name = re.sub(r'[<>"\']', '', name)
    
    # Limit length
    if len(name) > 50:
        name = name[:50]
    
    # Basic validation - only letters, numbers, spaces, and common punctuation
    if not re.match(r'^[a-zA-Z0-9\s\-_.,!]+$', name):
        return None
    
    return name.strip()

@app.route('/')
def hello():
    """
    Greet a user by name
    
    Query Parameters:
        name (str, optional): Name to greet. Defaults to 'World'
        
    Returns:
        JSON response with greeting message
    """
    try:
        name = request.args.get('name', 'World')
        
        # Validate and sanitize input
        validated_name = validate_name(name)
        if validated_name is None and name != 'World':
            logger.warning(f"Invalid name parameter received: {name}")
            return jsonify({
                'error': 'Invalid name parameter',
                'message': 'Name can only contain letters, numbers, spaces, and basic punctuation'
            }), 400
        
        final_name = validated_name if validated_name else 'World'
        
        logger.info(f"Greeting request for: {final_name}")
        
        return jsonify({
            'message': f'Hello, {final_name}!',
            'name': final_name
        })
        
    except Exception as e:
        logger.error(f"Error in hello endpoint: {str(e)}")
        return jsonify({
            'error': 'Internal server error'
        }), 500

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'flask-hello-app'
    })

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'error': 'Not found',
        'message': 'The requested resource was not found'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    logger.error(f"Internal server error: {str(error)}")
    return jsonify({
        'error': 'Internal server error',
        'message': 'Something went wrong on our end'
    }), 500

if __name__ == '__main__':
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    
    logger.info(f"Starting Flask app on {host}:{port} (debug={debug})")
    app.run(debug=debug, host=host, port=port)