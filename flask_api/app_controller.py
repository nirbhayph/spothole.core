# author: nirbhay pherwani. (https://nirbhay.me, pherwani37@gmail.com, np5318@rit.edu, https://github.com/nirbhayph)
# this is the main app controller for the flask application
# it contains all the routes that can be requested
# also makes sure cross origin resource requests are allowed
# it connects with the dark flow parent service and the mysql database service
# for performing the particular operations (validating images or communicating with the database)

# imports for flask, cors and parent and database service
from flask import Flask, request
from flask_cors import CORS
from json import dumps, loads
from parent_service import single_image_detection_results
from mysql_service import post_report_data, get_user_reports_data, post_report_comment_data, get_report_comments_data, \
    get_all_reports_data, get_user_profile_data, post_user_profile_data, get_authority_profile_data, \
    post_authority_profile_data, validate_authority, get_reports_for_authority, update_report_data, validate_user, update_user_status
from mail_service import send_email_spothole
import os
import random
import utility

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


# route for validating a single image
# accepts the image url for resource placed on the server
# to detect potholes on the image. connects with the dark-flow service
# at the backend.
@app.route('/api/detect/single', methods=['POST'])
def detect_potholes_in_image():
    data = request.get_json(silent=True)
    url = data.get('image_url')
    return single_image_detection_results(url)


# upload files using this route.
# renames the file and passes the url back for the uploaded file
@app.route('/api/upload', methods=['POST'])
def upload_files():
    if not os.path.exists(utility.IMG_UPLOADS_DIRECTORY):
        os.makedirs(utility.IMG_UPLOADS_DIRECTORY)

    file_names = []
    for key in request.files:
        file = request.files[key]
        fn = str(random.getrandbits(128)) + utility.DEFAULT_FILE_TYPE
        file_names.append(fn)
        try:
            file.save(os.path.join(utility.IMG_UPLOADS_DIRECTORY, fn))
        except:
            print('save fail: ' + os.path.join(utility.IMG_UPLOADS_DIRECTORY, fn))

    return dumps({'filename': [utility.IMG_UPLOADS_DISPLAY_URL + f for f in file_names]})


# submit a new report for the validated pothole
@app.route('/api/submit/report', methods=['POST'])
def submit_report():
    data = request.get_json(silent=True)
    return post_report_data(data["data"])


# get user reports
@app.route('/api/reports', methods=['POST'])
def get_user_reports():
    data = request.get_json(silent=True)
    return get_user_reports_data(data["data"])


# submit a comment
@app.route('/api/submit/report/comment', methods=['POST'])
def post_comment():
    data = request.get_json(silent=True)
    return post_report_comment_data(data["data"])


# get all comments by case id
@app.route('/api/reports/comments', methods=['POST'])
def get_report_comments():
    data = request.get_json(silent=True)
    return get_report_comments_data(data["data"])


# get all reports for all users
@app.route('/api/reports/all', methods=['POST'])
def get_all_reports():
    return get_all_reports_data()


# update user profile data
@app.route('/api/profile/update', methods=['POST'])
def post_user_profile():
    data = request.get_json(silent=True)
    return post_user_profile_data(data["data"])


# get user profile data
@app.route('/api/profile/data', methods=['POST'])
def get_user_profile():
    data = request.get_json(silent=True)
    return get_user_profile_data(data["data"])


# update authority profile data
@app.route('/api/profile/authority/update', methods=['POST'])
def post_authority_profile():
    data = request.get_json(silent=True)
    return post_authority_profile_data(data["data"])


# get authority profile data
@app.route('/api/profile/authority/data', methods=['POST'])
def get_authority_profile():
    data = request.get_json(silent=True)
    return get_authority_profile_data(data["data"])

# validate authority login
@app.route('/api/authority/check', methods=['POST'])
def validate_authority_profile():
    data = request.get_json(silent=True)
    return validate_authority(data["data"])


# geo near results for authority to get citizen reports,
# accepts authority email id as a param
@app.route('/api/authority/reports/geonear', methods=['POST'])
def get_reports_geonear_authority():
    data = request.get_json(silent=True)
    return get_reports_for_authority(data["data"])

# update report data (for authority)
# accepts case id, status and severity
@app.route('/api/authority/update/report', methods=['POST'])
def update_report_data_authority():
    data = request.get_json(silent=True)
    return update_report_data(data["data"])

# validate existing user
@app.route('/api/user/validate', methods=['POST'])
def validate_existing_user():
    data = request.get_json(silent=True)
    return validate_user(data["data"])

# update user status (for authority)
@app.route('/api/authority/update/user/status', methods=['POST'])
def update_existing_user_status():
    data = request.get_json(silent=True)
    return update_user_status(data["data"])

# send an email to the user (for authority)
# accepts user email id and message to be sent
@app.route('/api/authority/send/email', methods=['POST'])
def send_email():
    data = request.get_json(silent=True)
    return send_email_spothole(data["data"]["emailId"], data["data"]["message"], data["data"]["subject"])

# run app. use ssl and serve over https
# for ssl context please supply paths for both 
# the pem files (Here they are named as fullchain.pem and privkey.pem)
if __name__ == '__main__':
    app.run(host='0.0.0.0', ssl_context=('fullchain.pem', 'privkey.pem'))
