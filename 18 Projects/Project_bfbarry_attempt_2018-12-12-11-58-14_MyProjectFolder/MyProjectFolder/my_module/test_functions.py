import zipfile
import zlib
import sys
import time
import base64
from functions import simpleEncode, printEncode
import mock



    
def test_RLE1(): #tried to use mock to assert the following, but I continue receiving an OSError
    with mock.patch.object(__builtin__, 'input', lambda: 'some_input'):
        assert printEncode('aaaaaa') == 'a6'
    