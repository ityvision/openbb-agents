import logging
import logging.config

from openbb_agents.utils import map_openbb_collection_to_langchain_tools
from openbb_agents.agent import openbb_agent

import logging
import logging.config

logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'json': {
            '()': 'pythonjsonlogger.jsonlogger.JsonFormatter',
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
            'formatter': 'json',
        },
    },
    'loggers': {  # define loggers for specific modules
        'openbb_agents.agent': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'openbb_agents.utils': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
    'root': {  # root logger
        'handlers': ['console'],
        'level': 'WARNING',
    },
}

logging.config.dictConfig(logging_config)

openbb_tools = map_openbb_collection_to_langchain_tools(
    openbb_commands_root=[
        "/equity/fundamental",
        "/equity/compare",
        "/equity/estimates"
    ]
)

user_query = "Perform a fundamentals financial analysis of AMZN using the most recently available data. What do you find that's interesting?"
user_query = "Who are TSLA's peers?"
output = openbb_agent(openbb_tools, user_query)