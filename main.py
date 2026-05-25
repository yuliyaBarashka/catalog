from wsgiref.simple_server import make_server
from urllib.parse import parse_qs

def render_template(template_name):
    with open(f'templates/{template_name}', encoding='utf-8') as file:
        return file.read()

def application(environ, start_response):

    path = environ['PATH_INFO']
    method = environ['REQUEST_METHOD']

    # ---------------- POST ----------------
    if method == 'POST':

        try:
            size = int(environ.get('CONTENT_LENGTH', 0))
        except:
            size = 0

        body = environ['wsgi.input'].read(size).decode('utf-8')

        data = parse_qs(body)

        print('Получены данные:')
        print(data)

    # ---------------- ROUTES ----------------
    if path == '/':
        response = render_template('index.html')
        status = '200 OK'

    elif path == '/catalog':
        response = render_template('catalog.html')
        status = '200 OK'

    elif path == '/contacts':
        response = render_template('contacts.html')
        status = '200 OK'

    elif path == '/static/css/style.css':

        with open('static/css/style.css', encoding='utf-8') as file:
            response = file.read()

        status = '200 OK'

        headers = [('Content-type', 'text/css; charset=utf-8')]

        start_response(status, headers)

        return [response.encode('utf-8')]

    else:
        response = render_template('404.html')
        status = '404 NOT FOUND'

    headers = [('Content-type', 'text/html; charset=utf-8')]

    start_response(status, headers)

    return [response.encode('utf-8')]

if __name__ == '__main__':
    server = make_server('', 8000, application)

    print('Сервер запущен: http://127.0.0.1:8000')

    server.serve_forever()
