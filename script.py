import base64
from lxml import etree

from string import *

base64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('ascii')

f = open("response.xml", "w")
f.write(message)
f.close()

xml_str = message
root = etree.fromstring(xml_str)
print(etree.tostring(root, pretty_print=True).decode())