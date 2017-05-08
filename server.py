from bottle import route, run, request, HTTPResponse, template
import json

@route('/')
def root():
    return template('show', name="root")

@route('/v1/search/user')
def search():
    query = request.query.get('query')
    
    body = json.dumps([{"name":"Harry Potter"},{"name":"Draco Malfoy"},{"name":"Lord Voldemort"}])
    r = HTTPResponse(status=200, body=body)
    r.set_header("Content-Type", "application/json")
    return r

@route('/v1/search/tag')
def search():
    query = request.query.get('query')
    
    body = json.dumps([{"name":"#table"},{"name":"#desk"},{"name":"#char"}])
    r = HTTPResponse(status=200, body=body)
    r.set_header("Content-Type", "application/json")
    return r

@route('/v1/search/brand')
def search():
    query = request.query.get('query')
    
    body = json.dumps([{"name":"#table"},{"name":"#desk"},{"name":"#char"}])
    r = HTTPResponse(status=200, body=body)
    r.set_header("Content-Type", "application/json")
    return r

run(host='localhost', port=8080, debug=True, reloader=True)
