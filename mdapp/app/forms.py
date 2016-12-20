from flask_wtf import Form
from wtforms import StringField, BooleanField, SelectField
from wtforms.validators import DataRequired


class SongForm(Form):
	name = StringField('song_name', validators = [DataRequired()])
	ragam = StringField('song_ragam', validators = [DataRequired()])
	talam = StringField('song_talam', validators = [DataRequired()])
	artist = StringField('song_artist', validators = [DataRequired()])
	link = StringField('song_link', validators = [DataRequired()])

class EditForm(Form):
	name = StringField('song_name', validators = [DataRequired()])
	ragam = StringField('song_ragam', validators = [DataRequired()])
	talam = StringField('song_talam', validators = [DataRequired()])
	artist = StringField('song_artist', validators = [DataRequired()])
	link = StringField('song_link', validators = [DataRequired()])

class DeleteForm(Form):
	pass

class SortForm(Form):
	 sort_choice = SelectField(
        'Choice',
        choices=[('',''),('name', 'Name'),('ragam', 'Ragam'), ('talam', 'Talam'), ('artist', 'Artist'), ('varanam', 'Varanam')])
	 sort_val = StringField('sort_val')