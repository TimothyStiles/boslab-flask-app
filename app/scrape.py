def get_db_status(initial_search_request):
    '''
    initial_search_request = 'https://api.nal.usda.gov/ndb/search/?format=json&q=&sort=n&max=1&offset=0&api_key=DEMO_KEY'
    current_total = total number of items in usda database at the time of request
    current_sr = Standard Release version of the data at the time of request

    Returns {'current_total': current_total, 'current_sr': current_sr}
    '''
    usda_database_check = requests.get(initial_search_request)
    check_json = usda_database_check.json()
    current_total = check_json['list']['total']
    current_sr = check_json['list']['sr']
    return {'current_total': current_total, 'current_sr': current_sr}


def check_dbitem_changed(LAST_NDBNO_TOTAL, current_ndbno_total, LAST_SR, current_sr):  # TODO: convert to decorator
    '''Returns True if Database has a different number of items
    '''
    if LAST_NDBNO_TOTAL != current_ndbno_total:
        return True
    elif LAST_SR != current_sr:
        return True
    else:
        return False


def get_ndbno_list(search_api_request, formt, q, sort, mx, offset, API_KEY):
    '''This returns a list of ndbno's in the usda foods database
    '''
    search_object = requests.get(search_api_request)
    search_json = search_object.json()  # convert search_object to JSON

    ndbno_list_dict = search_json['list'][
        'item']  # ndbno_list_dict is a list of dictionaries, where each dictionary is a unique food item

    return ndbno_list_dict


def get_ndbno_full_report(report_api_request, ndbno_id):
    '''Returns JSON Full Report
    '''
    full_report = requests.get(report_api_request)
    full_report_json = full_report.json()
    return full_report_json

def create_food_json(full_report_json, )