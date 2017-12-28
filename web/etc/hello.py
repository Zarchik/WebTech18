def app(environ, start_response):
#        data = b"Hello, World! From Kirill\n"
	data = environ['QUERY_STRING']
        data = data.replace( "&", "\r\n")
        start_response("200 OK", [
            ("Content-Type", "text/plain")
#            ("Content-Type", "text/plain"),
#            ("Content-Length", str(len(data)))
        ])
#        return iter([data])
	return data
