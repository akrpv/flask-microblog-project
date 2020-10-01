from wtforms import Form, StringField, TextAreaField



class PostForm(Form):
    title = StringField('Title')
    tag = StringField('Tag')
    content = TextAreaField('Content')
