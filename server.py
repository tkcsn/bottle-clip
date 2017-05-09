from bottle import route, run, request, HTTPResponse, template, static_file
import json

@route('/')
def root():
    return template('show', name="root")

@route('/api/v1/users/search')
def search():
    query = request.query.get('q')
    
    body = json.dumps([{"name":"Harry Potter"},{"name":"Draco Malfoy"},{"name":"Lord Voldemort"}])
    r = HTTPResponse(status=200, body=body)
    r.set_header("Content-Type", "application/json")
    return r

@route('/api/v1/tags/search')
def search():
    query = request.query.get('q')
    
    body = json.dumps([{"name":"#table"},{"name":"#desk"},{"name":"#char"}])
    r = HTTPResponse(status=200, body=body)
    r.set_header("Content-Type", "application/json")
    return r

@route('/api/v1/brands/search')
def search():
    query = request.query.get('q')
    
    body = json.dumps([{"name":"#table"},{"name":"#desk"},{"name":"#char"}])
    r = HTTPResponse(status=200, body=body)
    r.set_header("Content-Type", "application/json")
    return r

@route('/imgs/<filename:path>')
def image(filename):
    res = static_file(filename, root='./imgs')
    return res

run(host='localhost', port=8080, debug=True, reloader=True)
