from pelican import signals as _signals
from pelican import readers as _readers


# monkey-patch EndDate processing
_readers.METADATA_PROCESSORS['enddate'] = _readers.METADATA_PROCESSORS['date']

def massage_metadata(generator, metadata):
    if metadata.get('category', None) == 'bootcamps':
        metadata['title'] = '{0}, {1}'.format(
            metadata['venue'],
            metadata['date'].strftime('%b %Y'))

def register():
    _signals.article_generator_context.connect(massage_metadata)
