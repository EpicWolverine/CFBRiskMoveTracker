import json


class SettingsManager:
    def __init__(self):
        with open("settings.json") as f:
            self.settings = json.load(f)

    def get_secrets(self):
        return self.settings["secrets"]

    def get_team_name(self):
        return self.settings["settings"]["team"]

    def get_verified_discord_role_name(self):
        return self.settings["settings"]["verified_discord_role_name"]
