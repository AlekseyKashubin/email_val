from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash




class Email:
    DB = 'email_schema'
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = """SELECT * FROM emails;"""
        results = connectToMySQL(cls.DB).query_db(query)
        all_emails = []
        for emails in results:
            all_emails.append( cls(emails) )
        return all_emails
    

    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        return connectToMySQL(cls.DB).query_db(query,data)
    


    @classmethod
    def delete_email(cls,data):
            query = """
            DELETE FROM emails WHERE id = %(id)s ;
            """
            results = connectToMySQL(cls.DB).query_db(query, data)
            return results



    @staticmethod
    def is_valid(email):
        is_valid = True
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        results = connectToMySQL(Email.DB).query_db(query,email)
        if len(results) >= 1:
            flash("Email already taken.")
            is_valid=False
        if not EMAIL_REGEX.match(email['email']):
            flash("Invalid Email.")
            is_valid=False
        
        return is_valid
    

# flash('First name must be at least 3 character long', 'registration')
# {% with messages = get_flashed_messages(category_filter=['registration']) %}