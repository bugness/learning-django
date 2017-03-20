def app(environ, start_response):
    query = environ.get('QUERY_STRING').replace('?', '')
    data = [bytes(i + '\n', 'ascii') for i in query.split('&')]
    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter(data)
