from codecs import open
import os
import uuid


class Model(object):
	def save_image(self, drawn_digit, image):
		filename = 'digit' + str(drawn_digit) + '__' + str(uuid.uuid1()) + '.jpg'
		with open('tmp/' + filename, 'wb') as f:
			f.write(image)
			
		print('Image written')

		return ('Image saved successfully with the name {0}'.format(filename))
