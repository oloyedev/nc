from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) 
 # Update to the specific domain for security

# List of eligible Solana wallet addresses
ELIGIBLE_WALLETS = {
    "F7Dw4eUMPR5vg75nYSkAPqTVqWMoE9GRDtK8e1kH6GKu",
    "Cp6pS7QgZRC2KLRgQ8NyNYF6vwE5zBtkVAbCnNHpAkfF",
    "5cBTqwx4pC4vV3G8cb9SLpJLyh2ShcD9ABkpeE9H3sgR",
}

@app.route("/check-eligibility", methods=["POST"])
def check_eligibility():
    data = request.get_json()
    wallet = data.get("wallet")

    if not wallet:
        return jsonify({"success": False, "message": "Wallet address is required"}), 400

    if wallet in ELIGIBLE_WALLETS:
        return jsonify({"success": True, "eligible": True, "message": "Wallet is eligible"})
    else:
        return jsonify({"success": True, "eligible": False, "message": "Wallet is not eligible"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

