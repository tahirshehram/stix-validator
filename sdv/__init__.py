import os
import json
from version import __version__

_PKG_DIR = os.path.dirname(__file__)
XSD_ROOT = os.path.abspath(os.path.join(_PKG_DIR, 'xsd'))


class ValidationError(Exception):
    pass


class ValidationResult(object):
    def __init__(self, is_valid=False):
        self.is_valid = is_valid

    @property
    def is_valid(self):
        return self._is_valid

    @is_valid.setter
    def is_valid(self, value):
        self._is_valid = bool(value)

    def as_dict(self):
        return {'result': self.is_valid}

    def as_json(self):
        return json.dumps(self.as_dict())