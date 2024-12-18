import json

class ConfigData(object):
    @staticmethod
    def load_config(file_path):
        """Loads configuration and sets class-level attributes."""
        try:
            with open(file_path, 'r') as file:
                config = json.load(file)
                for key, value in config.items():
                    setattr(ConfigData, key, value)
        except Exception as e:
            print(f"Error loading config: {e}")