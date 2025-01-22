BOT_NAME = 'pep_parse'

DIR_FOR_RESULT = 'results'

NEWSPIDER_MODULE = f'{BOT_NAME}.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

FEEDS = {
    f'{DIR_FOR_RESULT}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status']
    }
}
