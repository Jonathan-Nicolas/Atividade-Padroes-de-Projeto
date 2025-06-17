import os
import re

class SiteNameHandler:
    
    def validate(self, name: str) -> bool:
        return bool(re.match(r"^\[[^\]]+\]\s", name))

    def action(self, name: str) -> str:
        return re.sub(r"^\[[^\]]+\]\s", "", name)
