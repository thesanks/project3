import wtforms
from wtforms.validators import DataRequired
from models import Entry, Tag

class TagField(wtforms.StringField):
    def _value(self):
        if self.data:
            # return as a comma-separated list.
            return ', '.join([tag.name for tag in self.data])
        return ''

    def get_tags_from_string(self, tag_string):
        raw_tags = tag_string.split(',')

        # Filter out empty tag names.
        tag_names = [name.strip() for name in raw_tags if name.strip()]

        # Query and retrieve any tags already saved.
        existing_tags = Tag.query.filter(Tag.name.in_(tag_names))

        # Which tag names are new?
        new_names = set(tag_names) - set([tag.name for tag in existing_tags])

        # Create list of unsaved Tag instances for  new tags.
        new_tags = [Tag(name=name) for name in new_names]

        # Return all existing tags + all new, unsaved tags.
        return list(existing_tags) + new_tags

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = self.get_tags_from_string(valuelist[0])
        else:
            self.data = []

class EntryForm(wtforms.Form):
    title = wtforms.StringField('Title', validators=[DataRequired()])
    body  = wtforms.TextAreaField('Body', validators=[DataRequired()])
    status = wtforms.SelectField('Entry status', choices=(
            (Entry.STATUS_PUBLIC, 'Public'),
            (Entry.STATUS_DRAFT,  'Draft')), coerce=int)
    tags = TagField('Tags', description='Separate multiple tags with commas.')

    def save_entry(self, entry):
        self.populate_obj(entry)
        entry.generate_slug()
        return entry

class ImageForm(wtforms.Form):
    file = wtforms.FileField('Image file')
