import qrcode
import qrcode.image.svg
from io import BytesIO
context={}
factory = qrcode.image.svg.SvgImage
img = qrcode.make("mamad", image_factory=factory, box_size=20)
stream = BytesIO()
img.save(stream)
context["svg"] = stream.getvalue().decode()