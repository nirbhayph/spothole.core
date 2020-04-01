# author: nirbhay pherwani. (https://nirbhay.me, pherwani37@gmail.com, np5318@rit.edu, https://github.com/nirbhayph)
# this is the mysql service used to communicate with the backend. it involves communicating with tables in the spothole database
import mysql.connector
import random
from datetime import datetime
from flask import jsonify

# connector method for the spothole db
def connect():
    return mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="root",
      database="spothole"
    )

# post new report data
def post_report_data(data):
    db = connect()
    cursor = db.cursor()
    latitude = data["locationLatLng"]["lat"]
    longitude = data["locationLatLng"]["lng"]
    sql = "INSERT INTO __reports__ (case_id, description, address, imageURL, latitude, longitude, severity, userId, status, created_date, location_point) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, POINT(" + str(latitude) + "," + str(longitude) + "))"
    val = (str(random.getrandbits(32)), data["description"], data["location"], data["imageURL"], latitude, longitude, data["severity"], data["userId"], "submitted", datetime.utcnow())
    cursor.execute(sql, val)
    db.commit()
    return str(cursor.rowcount) + " record inserted."

# get reports data for a user
def get_user_reports_data(data):
    db = connect()
    cursor = db.cursor()

    sql = "SELECT * FROM __reports__ WHERE userId = %s ORDER BY last_updated DESC"
    userId = (data["userId"], )

    cursor.execute(sql, userId)

    results = cursor.fetchall()

    payload = []
    content = {}
    for result in results:
       content = {'case_id': result[0], 'description': result[1], 'imageURL': result[2], 'latitude': result[3], 'longitude': result[4], 'severity': result[5], 'userId': result[6], 'status': result[7], 'created_date': result[8], 'last_status_update': result[9], 'location': result[10]}
       payload.append(content)
       content = {}
    return jsonify(payload)

# post a comment on a report
def post_report_comment_data(data):
    db = connect()
    cursor = db.cursor()
    sql = "INSERT INTO __report_comments__ (user_type, comment_id, comment_text, case_id) VALUES (%s, %s, %s, %s)"
    val = (data["userType"], str(random.getrandbits(128)), data["commentText"], data["caseId"])
    cursor.execute(sql, val)
    db.commit()
    return str(cursor.rowcount) + " record inserted."

# get report comments for a case id
def get_report_comments_data(data):
    db = connect()
    cursor = db.cursor()

    sql = "SELECT user_type, comment_text, comment_date_time FROM __report_comments__ WHERE case_id = %s ORDER BY comment_date_time ASC"
    caseId = (data["caseId"], )

    cursor.execute(sql, caseId)

    results = cursor.fetchall()

    payload = []
    content = {}
    for result in results:
       content = {'userType': result[0], 'commentText': result[1], 'commentDateTime': result[2]}
       payload.append(content)
       content = {}
    return jsonify(payload)

# get all reports data for all users
def get_all_reports_data():
    db = connect()
    cursor = db.cursor()

    sql = "SELECT * FROM __reports__"

    cursor.execute(sql)

    results = cursor.fetchall()

    payload = []
    content = {}
    for result in results:
       content = {'case_id': result[0], 'description': result[1], 'imageURL': result[2], 'latitude': result[3], 'longitude': result[4], 'severity': result[5], 'userId': result[6], 'status': result[7], 'created_date': result[8], 'last_status_update': result[9], 'location': result[10]}
       payload.append(content)
       content = {}
    return jsonify(payload)

# update profile data
def post_user_profile_data(data):
    db = connect()
    cursor = db.cursor()
    sql = "INSERT INTO __public_users__ (user_id, email_id, name, photo_url, badge, status) VALUES (%s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE name=%s, photo_url=%s"
    val = (data["userId"], data["emailId"], data["name"], data["photoURL"], "LIVE_VALUE", "allowed", data["name"], data["photoURL"])
    cursor.execute(sql, val)
    db.commit()
    return str(cursor.rowcount) + " records affected."

# get a particular user's profile data
def get_user_profile_data(data):
    db = connect()
    cursor = db.cursor()

    sql = "SELECT * FROM __public_users__ WHERE user_id = %s"
    userId = (data["userId"], )

    cursor.execute(sql, userId)

    results = cursor.fetchall()

    payload = []
    content = {}
    for result in results:
       content = {'userId': result[0], 'email': result[1], 'name': result[2], 'badge': result[3], 'photoURL': result[4], 'status': result[5]}
       payload.append(content)
       content = {}
    return jsonify(payload)

# validate user signing in (uses user id as a param)
def validate_user(data):
    db = connect()
    cursor = db.cursor()

    sql = "SELECT status FROM __public_users__ WHERE email_id = %s"
    email_id = (data["emailId"], )

    cursor.execute(sql, email_id)

    results = cursor.fetchall()
    for result in results:
        return result[0]

    return "allowed"

# update user status
def update_user_status(data):
    db = connect()
    cursor = db.cursor()

    sql = "UPDATE __public_users__ SET status = %s WHERE user_id = %s"
    user_id = (data["status"], data["userId"], )

    cursor.execute(sql, user_id)
    db.commit()

    return str(cursor.rowcount) + " records affected."

# validate authority signing in (uses email id as a param)
def validate_authority(data):
    db = connect()
    cursor = db.cursor()

    sql = "SELECT authority_id FROM __authorities__ WHERE email_id = %s"
    emailId = (data["emailId"], )

    cursor.execute(sql, emailId)

    results = cursor.fetchall()
    count = len(results)
    if(count < 1):
        return "Unauthorized Login"
    else:
        return "Authorized Login"

# update authority's profile data
def post_authority_profile_data(data):
    db = connect()
    cursor = db.cursor()
    sql = "INSERT INTO __authorities__ (authority_id, email_id, name, photo_url) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE name=%s, photo_url=%s"
    val = (data["authorityId"], data["emailId"], data["name"], data["photoURL"], data["name"], data["photoURL"])
    cursor.execute(sql, val)
    db.commit()
    return str(cursor.rowcount) + " records affected."

# get a particular authority's profile data (uses authority id as a param)
def get_authority_profile_data(data):
    db = connect()
    cursor = db.cursor()

    sql = "SELECT * FROM __authorities__ WHERE authority_id = %s"
    authority_id = (data["authorityId"], )

    cursor.execute(sql, authority_id)

    results = cursor.fetchall()

    payload = []
    content = {}
    for result in results:
       content = {'authority_id': result[0], 'email': result[1], 'name': result[2], 'photoURL': result[3], 'latitude': result[4], 'longitude': result[5], 'address': result[6]}
       payload.append(content)
       content = {}
    return jsonify(payload)

# geo near implementation for citizen reports for authority
def get_reports_for_authority(data):
    db = connect()
    cursor = db.cursor()

    sql = "SELECT * FROM __authorities__ WHERE authority_id = %s"
    authority_id = (data["authorityId"], )
    cursor.execute(sql, authority_id)

    authority = cursor.fetchall()

    payload = []
    for authority_item in authority:
       authority_latitude = authority_item[4]
       authority_longitude = authority_item[5]
       sql = "SELECT * FROM __reports__ JOIN __public_users__ WHERE (st_distance_sphere(location_point, POINT(" + str(authority_latitude) + "," + str(authority_longitude) + ")) < 5000) AND (__reports__.userId = __public_users__.user_id)"
       cursor.execute(sql)
       reports = cursor.fetchall()
       content = {}
       for result in reports:
        content = {'case_id': result[0], 'description': result[1], 'imageURL': result[2], 'latitude': result[3], 'longitude': result[4], 'severity': result[5], 'userId': result[6], 'status': result[7], 'created_date': result[8], 'last_status_update': result[9], 'location': result[10], 'user_email': result[13], 'user_full_name': result[14], 'user_photo_url':result[16], 'user_status': result[17]}
        payload.append(content)
        content = {}
    return jsonify(payload)

# update report data (for authority)
def update_report_data(data):
    db = connect()
    cursor = db.cursor()
    sql = "UPDATE __reports__ SET severity = %s, status = %s WHERE case_id=%s"
    val = (data["severity"], data["status"], data["caseId"])
    cursor.execute(sql, val)
    db.commit()
    return str(cursor.rowcount) + " record(s) updated."