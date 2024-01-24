from dataclasses import dataclass

from django.contrib.admin.utils import get_deleted_objects

@dataclass
class Spam:
    first_name: str
    last_name: str
