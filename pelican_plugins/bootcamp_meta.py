from pelican import signals as _signals


def massage_metadata(generator, metadata):
    if metadata.get('category', None) == 'bootcamps':
        metadata['title'] = '{0}, {1}'.format(
            metadata['venue'],
            metadata['date'].strftime('%b %Y'))

def register():
    _signals.article_generate_context.connect(massage_metadata)
