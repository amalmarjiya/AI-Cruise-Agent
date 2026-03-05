import os
from app import app  # your Flask instance must be named "app"

port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port, debug=False)