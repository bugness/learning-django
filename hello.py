def app(environ, start_response):
    query = environ.get('QUERY_STRING').replace('?', '')
    data = [str(i) + '\n' for i in query.split('&')]
    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain'),
    ]
    start_response(status, response_headers)
    return iter(data)
