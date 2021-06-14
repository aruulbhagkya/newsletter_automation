"""
This Module Contains the Form classes for Add articles form
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, FormField
from wtforms.validators import DataRequired, Length
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from . models import Article_category,Articles,db
from sqlalchemy.orm import sessionmaker



def choice_query():
    
    return Article_category.query

"""
def choice_url(category):
    print("Here in choice_url",category)
    return db.session.query(Articles).filter(Articles.category_id == 5)
"""

class ArticleForm(FlaskForm):
    "Class for articles form"
    
    category_id= QuerySelectField(query_factory=choice_query, allow_blank=True,get_label='category_name')
    #title = StringField('Title')
    #url= QuerySelectField(query_factory=choice_url, allow_blank=True,get_label='url')
    url = SelectField('url', choices=[])
    title = SelectField('Title',choices=[])
    description = TextAreaField('Description')
    reading_time = StringField('Reading Time')
    add_more = SubmitField('Add More Articles')
    added_articles = my_field = TextAreaField('Added Articles:', render_kw={'readonly': True})
    opener = TextAreaField('Opener')
    preview_text = TextAreaField('Preview Text',render_kw={'maxlength': 150})
    schedule = SubmitField('Schedule')
