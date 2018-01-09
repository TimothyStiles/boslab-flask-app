# Database information
POSTGRES = {
    'user': 'ifrancium',
    'pw': 'password',
    'db': 'usda',
    'host': 'localhost',
    'port': '5432',
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@{}:{}/{' \
                                        '}'.format(POSTGRES['user'],
                                                   POSTGRES['pw'],
                                                   POSTGRES['host'],
                                                   POSTGRES['port'],
                                                   POSTGRES['db'])


SQLALCHEMY_TRACK_MODIFICATIONS = True

# variables for the USDA search API
LAST_NDBNO_TOTAL = 200000
LAST_SR = 28
current_ndbo_total = 0
current_sr = 0
API_KEY = '7WqOHQdC2shEfBrx25bIEwxBkvUkYTHMoHYlLWL8' #1000 requests/hour
q = ''
ds = ''
fg = ''
sort = 'n'
mx = 35 # max is 1500
offset = 0
formt = 'json'
q = ''
typ = 'f'
ndbno_id = 0


# special api request to get meta information on database (total number of items, standard reference version)
initial_search_request = 'https://api.nal.usda.gov/ndb/search/?format=json&q=&sort=n&max=1&offset=0&api_key=7WqOHQdC2shEfBrx25bIEwxBkvUkYTHMoHYlLWL8'

# search API
search_api_request = 'https://api.nal.usda.gov/ndb/search/?format={}&q={}&sort={}&max={}&offset={}&api_key={}'.format(formt, q, sort, mx, offset, API_KEY)

# Get JSON report with API
report_api_request = 'https://api.nal.usda.gov/ndb/reports/?ndbno={}&type={}&format={}&api_key={}'.format(ndbno_id, typ, formt, API_KEY)