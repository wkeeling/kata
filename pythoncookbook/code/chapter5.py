import tempfile
import os
from functools import partial


def iter_records(filepath, record_size=32):
    with open(filepath, 'rb') as f:
        yield from iter(partial(f.read, record_size), b'')


def read_into_buffer(filepath):
    buf = bytearray(os.path.getsize(filepath))
    with open(filepath, 'rb') as f:
        f.readinto(buf)
    return buf


def create_temp_file():
    return tempfile.TemporaryFile('w+t')
