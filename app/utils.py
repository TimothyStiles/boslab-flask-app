# This file contains generic functions

def update(object):
    """
    This function looks through new sr version and updates food item
    :param object:
    :return:
    """
    email = None
    if request.method == 'POST':
        email = request.form['email']
        # Check that email does not already exist (not a great query, but works)
        if not db.session.query(User).filter(User.email == email).count():
            reg = User(email)
            db.session.add(reg)
            db.session.commit()
            return render_template('success.html')
    return render_template('index.html')

def create_new_food_item(food_json):
    """
    creates new database instance of food item using data from food_json
    :param food_json: JSON doc with all information on...
    :return:
    """



