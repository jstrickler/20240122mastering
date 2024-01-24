import dataclasses
import django.contrib.admin.utils

@dataclasses.dataclass
class Spam:
    first_name: str
    last_name: str
