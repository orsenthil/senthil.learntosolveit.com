# -*- coding: utf-8 -*-

# Copyright © 2020 Roberto Alsina and others.

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
import requests

import pypandoc
import pydevto

from nikola import utils
from nikola.plugin_categories import Command

LOGGER = utils.get_logger("Devto")


class CommandDevto(Command):
    """
    This class is based on the package medium (https://plugins.getnikola.com/v8/medium/)
    """

    name = "devto"
    needs_config = True
    doc_usage = ""
    doc_purpose = "Publish your articles to Dev.to"

    def _execute(self, options, args):
        """Publish to Dev.to."""

        if not os.path.exists("devto.json"):
            LOGGER.error("Please put your credentials in devto.json as described in the README.")
            return False
        with open("devto.json") as inf:
            creds = json.load(inf)
        api = pydevto.PyDevTo(api_key=creds["TOKEN"])

        articles = api.articles()
        self.site.scan_posts()

        posts = self.site.timeline

        devto_titles = {item["title"] for item in articles}
        to_post = [
            post
            for post in posts
            if post.title() not in devto_titles and post.meta("devto") and (post.meta("devto").lower() not in ["no", "false", "0"])
        ]

        if len(to_post) == 0:
            LOGGER.info("Nothing new to post...")

        for post in to_post:
            try:
                with open(post.source_path, 'r', encoding='utf-8') as file:
                    data = file.read()

                    # Handle different file types
                    if post.source_ext() == ".md":
                        content = "".join(data)
                    elif post.source_ext() == ".rst":
                        content = pypandoc.convert_file(post.source_path, to="gfm", format="rst")
                    elif post.source_ext() == ".ipynb":
                        content = pypandoc.convert_file(post.source_path, to="gfm", format="ipynb")
                    else:
                        LOGGER.warning(f"Unsupported file format: {post.source_ext()} for {post.source_path}")
                        content = data

                    # Debug: Print values before API call
                    title = post.title()
                    canonical_url = post.permalink(absolute=True)
                    tags = post.tags if post.tags else []
                    
                    LOGGER.info(f"Title: {title}")
                    LOGGER.info(f"Content length: {len(content)}")
                    LOGGER.info(f"Canonical URL: {canonical_url}")
                    LOGGER.info(f"Tags: {tags}")

                    # Ensure we have required fields
                    if not title or not content:
                        LOGGER.error(f"Missing required fields for {post.source_path}: title={title}, content_length={len(content) if content else 0}")
                        continue

                    # Create article using direct API call with proper structure
                    article_data = {
                        "article": {
                            "title": title,
                            "body_markdown": content,
                            "published": True,
                            "canonical_url": canonical_url,
                            "tags": tags,
                        }
                    }
                    
                    response = requests.post(
                        "https://dev.to/api/articles",
                        json=article_data,
                        headers={"api-key": creds["TOKEN"]},
                        timeout=30
                    )
                    m_post = response.json()
                    
                    # Debug: Show the full response
                    LOGGER.info(f"API Response: {m_post}")
                    
                    # Handle different possible response structures
                    if isinstance(m_post, dict):
                        if 'url' in m_post:
                            url = m_post['url']
                        elif 'path' in m_post:
                            url = f"https://dev.to{m_post['path']}"
                        elif 'slug' in m_post:
                            url = f"https://dev.to/{m_post.get('user', {}).get('username', 'unknown')}/{m_post['slug']}"
                        else:
                            url = "URL not found in response"
                            LOGGER.warning(f"Available keys in response: {list(m_post.keys())}")
                    else:
                        url = "Invalid response format"
                    
                    LOGGER.info("Published {} to {}".format(post.meta("slug"), url))
                    
            except Exception as e:
                LOGGER.error(f"Error publishing {post.source_path}: {str(e)}")
                # Print more details about the error
                import traceback
                LOGGER.error(f"Full traceback: {traceback.format_exc()}")
                continue