from tornado import web, httpserver, ioloop, gen

import video


class Application(web.Application):
	def __init__(self):
		handlers = [(r'/vstream', StreamHandler)]
		self.cam = video.USBCamera()
		
		super(Application, self).__init__(handlers, debug=True)


class StreamHandler(web.RequestHandler):
	@web.asynchronous
	@gen.coroutine
	def get(self):
		"""
		set http stream headers
		"""
		self.set_header('Cache-Control',
						'no-store, no-cache, must-revalidate, pre-check=0, post-check=0, max-age=0')
		self.set_header('Connection', 'close')
		self.set_header('Content-Type', 
					'multipart/x-mixed-replace;boundary=--boundarydonotcross')

		while True:
			img = self.application.cam.get_frame()

			self.write("--boundarydonotcross\n")
			self.write("Content-type: image/jpeg\r\n")
			self.write("Content-length: %s\r\n\r\n" % len(img))
			self.write(str(img))

			yield gen.Task(self.flush)


if __name__ == '__main__':
	server = httpserver.HTTPServer(Application())
	server.listen(8080)
	ioloop.IOLoop.current().start()