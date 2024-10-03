from flask import Blueprint, jsonify
from .policy_details_retriever import retrieve_policy_details_route
from .logger import logger


def configure_routes(app):
    policy_blueprint = Blueprint('policy_blueprint', __name__)

    # Add the policy details retrieval route
    policy_blueprint.route('/retrievePolicyDetails', methods=['POST'])(retrieve_policy_details_route)

    # Add a health check route
    @policy_blueprint.route('/health', methods=['GET'])
    def health_check():
        logger.info("Health check endpoint hit.")
        return jsonify({"message": "API is running"}), 200

    # Register the blueprint
    app.register_blueprint(policy_blueprint, url_prefix='/submissionIntakeAPI')

    logger.info("Routes configured successfully.")
