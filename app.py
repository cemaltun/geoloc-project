from bottle import route, template, run, static_file, request, response
import http.client
import urllib
import json

@route('/search', method=['GET', 'POST'])
def search():
    if request.POST:
        latitude = request.forms.get('latitude')
        longitude = request.forms.get('longitude')

        p = { 'key': 'GBA3BV7FYSKKUE19RX7R4NBULKSZDCJQ', 'format': 'json', 'lat': latitude, 'lng': longitude }

        conn = http.client.HTTPConnection("api.geodatasource.com")
        conn.request("GET", "/city?" + urllib.parse.urlencode(p))
        res = conn.getresponse()
        data = json.load(res)
        return template('result', data=data)
    return template('ticket_form')

@route('/css/<filename>')
def send_css(filename):
    return static_file(filename, root='static/css')

run(host='localhost', port=8080, debug=True)
