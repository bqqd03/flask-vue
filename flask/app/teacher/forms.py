from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Length


class EditProfileForm(FlaskForm):
    name = StringField('Real name', validators=[Length(0, 64)])
    Age = StringField('Age', validators=[Length(0, 64)])
    Major = StringField('Age', validators=[Length(0, 64)])
    Class = StringField('Age', validators=[Length(0, 64)])
    submit = SubmitField('Submit')

