"""
Flask application for ML Project
"""

from flask import Flask, render_template, request, jsonify
from src.mlProject.utils.logger import get_logger

logger = get_logger(__name__)

# Create Flask app
app = Flask(__name__, template_folder='templates')

logger.info("Flask application initialized")


@app.before_request
def log_request():
    """Log all incoming requests"""
    logger.info(f"Request: {request.method} {request.path}")


@app.after_request
def log_response(response):
    """Log all responses"""
    logger.info(f"Response: {response.status_code} for {request.path}")
    return response


@app.route('/', methods=['GET'])
def index():
    """Home page"""
    try:
        logger.info("Rendering home page")
        return render_template('index.html')
    except Exception as e:
        logger.error(f"Error rendering home page: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500


@app.route('/predict', methods=['POST'])
def predict():
    """Prediction endpoint"""
    try:
        data = request.get_json()
        logger.info(f"Prediction request received with data: {data}")
        
        # TODO: Add prediction logic here
        logger.warning("Prediction logic not yet implemented")
        
        return jsonify({
            "status": "success",
            "message": "Prediction endpoint ready"
        })
    except Exception as e:
        logger.error(f"Error in prediction: {str(e)}")
        return jsonify({"error": str(e)}), 400


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    logger.debug("Health check requested")
    return jsonify({"status": "healthy", "message": "Server is running"}), 200


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    logger.warning(f"404 Error: {request.path} not found")
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    logger.error(f"500 Internal Server Error: {str(error)}")
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    logger.info("=" * 60)
    logger.info("Starting Flask application...")
    logger.info("=" * 60)
    
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except Exception as e:
        logger.error(f"Failed to start Flask app: {str(e)}")
        exit(1)
