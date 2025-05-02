"""
Settting up the fine-grained configuration.
  - Superset's configuration is done via its 'config.py' file.
   - To see this file + get a look at the defaults it sets look at: https://github.com/apache/superset/blob/master/superset/config.py
  - In this file, we will let the defaults be created, then override anything we want.
"""
FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
}

ENABLE_PROXY_FIX = True
SECRET_KEY = "when in digrace with men and fortune's eyes, I all alone bemoan my outcast state and trouble deaf heaven with bottless cries"
