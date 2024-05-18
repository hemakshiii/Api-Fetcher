from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__, static_url_path='/static')
baseUrl = "https://devapi.beyondchats.com/api/get_message_with_sources"

def main_request(baseUrl, x):
    r = requests.get(baseUrl + f'?page={x}')
    return r.json()

def get_total_pages(response):
    total_items = response['data']['total']
    items_per_page = response['data']['per_page']
    total_pages = (total_items + items_per_page - 1) // items_per_page
    return total_pages

def parse_json(response):
    charlist = []
    for item in response['data']['data']:
        for source in item['source']:
            char = {
                'id': source['id'],
                'link': source['link'],
            }
            charlist.append(char)
    return charlist

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_data', methods=['GET'])
def fetch_data():
    mainlist = []
    data = main_request(baseUrl, 1)  
    total_pages = get_total_pages(data)

    for x in range(1, total_pages + 1):
        mainlist.extend(parse_json(main_request(baseUrl, x)))

    return jsonify(mainlist)

if __name__ == '__main__':
    app.run(debug=True)

