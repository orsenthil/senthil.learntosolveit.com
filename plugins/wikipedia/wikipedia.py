# -*- coding: utf-8 -*-

# Copyright © 2023 Lorenzo Rovigatti.

# Permission is hereby granted, free of charge, to any
# person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the
# Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the
# Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import json
import os
import time

from nikola.plugin_categories import ShortcodePlugin
from nikola.utils import req_missing

try:
    import wikipediaapi
except ImportError:
    wikipediaapi = None

_CACHE_FILE = os.path.join(os.path.dirname(__file__), '..', '..', 'cache', 'wikipedia_cache.json')


def _load_cache():
    if os.path.exists(_CACHE_FILE):
        with open(_CACHE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def _save_cache(cache):
    os.makedirs(os.path.dirname(_CACHE_FILE), exist_ok=True)
    with open(_CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)


class WikipediaShortcodePlugin(ShortcodePlugin):
    """Return an HTML element containing the summary of a Wikipedia article that can be styled as a tooltip"""

    name = "wikipedia"

    def _error(self, msg):
        self.logger.error(msg)
        return '<div class="text-error">{}</div>'.format(msg)

    def handler(self, article, text=None, site=None, data=None, lang='en', post=None):
        if wikipediaapi is None:
            msg = req_missing(['wikipediaapi'], 'use the wikipedia shortcode', optional=True)
            return self._error(msg)

        cache_key = '{}:{}'.format(lang, article)
        cache = _load_cache()

        if cache_key in cache:
            url = cache[cache_key]['url']
            summary = cache[cache_key]['summary']
        else:
            wiki_api = wikipediaapi.Wikipedia(
                "{0} ({1})".format(self.site.config['BLOG_AUTHOR'], self.site.config['BLOG_AUTHOR']), lang
            )

            wiki_page = None
            for attempt in range(4):
                try:
                    wiki_page = wiki_api.page(article)
                    _ = wiki_page.exists()  # trigger the HTTP fetch
                    break
                except Exception as e:
                    if attempt < 3:
                        sleep_secs = 10 * (2 ** attempt)  # 10, 20, 40 seconds
                        self.logger.warning(
                            'Wikipedia fetch for "{}" failed (attempt {}), retrying in {}s: {}'.format(
                                article, attempt + 1, sleep_secs, e
                            )
                        )
                        time.sleep(sleep_secs)
                    else:
                        return self._error('Wikipedia fetch for "{}" failed after retries: {}'.format(article, e))

            if not wiki_page.exists():
                return self._error('Wikipedia page "{0}" not found'.format(article))

            url = wiki_page.fullurl
            summary = wiki_page.summary.split('\n')[0]
            summary = "".join(x.strip() for x in summary.split("(listen);"))

            # Re-read before writing to avoid clobbering entries saved by concurrent handlers
            fresh_cache = _load_cache()
            fresh_cache[cache_key] = {'url': url, 'summary': summary}
            _save_cache(fresh_cache)

        if text is None:
            text = article

        tooltip = """
        <span class="wikipedia_tooltip"><a href="{0}" target="_blank">{1}</a>
            <span class="wikipedia_summary">
            <a href="{0}" target="_blank" class="wikipedia_wordmark">
              <img src="https://upload.wikimedia.org/wikipedia/commons/b/bb/Wikipedia_wordmark.svg">
              <span class="wikipedia_icon"></span>
            </a>
            {2}
            </span>
        </span>""".format(url, text, summary)

        return tooltip, []
