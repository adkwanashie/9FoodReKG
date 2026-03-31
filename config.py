import os

# -----------------------------------------------------
# Streamlit UI Theme Settings
# -----------------------------------------------------
THEME_CONFIG = {
    "base": "light",
    "primaryColor": "#4CAF50",
    "backgroundColor": "#F8F9FA",
    "secondaryBackgroundColor": "#E3E6E8",
    "textColor": "#333333",
    "font": "sans serif"
}

# -----------------------------------------------------
# Server Configuration
# -----------------------------------------------------
SERVER_CONFIG = {
    "maxUploadSize": 500,  # File upload limit (MB)
    "port": 8503,          # Streamlit server port
    "headless": False,
    "enableCORS": True,
    "runOnSave": True
}

# -----------------------------------------------------
# Logging Configuration
# -----------------------------------------------------
LOGGING_CONFIG = {
    "level": os.getenv("LOG_LEVEL", "info"),  # Dynamic logging level
    "log_to_file": True,
    "file_path": os.path.join(os.getcwd(), "logs", "app.log")
}

# -----------------------------------------------------
# Kaggle Dataset Adapter
# -----------------------------------------------------
#KAGGLE_CONFIG = {
#    "dataset_handle": os.getenv("KAGGLE_DATASET", "neelghoshal/therapist-patient-conversation-dataset")
#}

# -----------------------------------------------------
# Paths & API Keys
# -----------------------------------------------------
CONFIG_PATHS = {
    "cache_dir": os.path.join(os.getcwd(), "cache"),
    "output_dir": os.path.join(os.getcwd(), "output"),
}

API_KEYS = {
    "openai": os.getenv("OPENAI_API_KEY", "your-default-openai-key"),
    "mapbox": os.getenv("MAPBOX_API_KEY", "your-default-mapbox-key"),
    "neo4j": os.getenv("NEO4J_PASSWORD", "your-secure-neo4j-password")
}

# -----------------------------------------------------
# Neo4j Configuration (New Section)
# -----------------------------------------------------
NEO4J_CONFIG = {
    "uri": os.getenv("NEO4J_URI", "neo4j://127.0.0.1:7687"),
    "user": os.getenv("NEO4J_USER", "neo4j"),
    "password": os.getenv("NEO4J_PASSWORD", "your-secure-password")
}

# -----------------------------------------------------
# Data Visualization Defaults (New Section)
# -----------------------------------------------------
VISUALIZATION_CONFIG = {
    "color_palette": "coolwarm",
    "plot_theme": "whitegrid",  # Options: "darkgrid", "whitegrid", etc.
    "altair_interactivity": True  # Enable dynamic Altair charts
}

# -----------------------------------------------------
# Function to Load Configurations
# -----------------------------------------------------
def get_config(section):
    return globals().get(section.upper(), {})

if __name__ == "__main__":
    print("Neo4j Connection:", NEO4J_CONFIG["uri"])