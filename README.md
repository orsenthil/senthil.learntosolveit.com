# <https://senthil.learntosolveit.com>

This is my personal blog, built with the static site generator [Nikola](https://getnikola.com/).

## Local build and deploy

```bash
source ~/virtual-envs/nikola/bin/activate
source ~/virtual-envs/nodeenv/bin/activate
nikola build
nikola deploy
```

## Remote workflows

### Publish (`.github/workflows/publish.yml`)

Triggered on every push to `master`. Builds the site with `nikola build` and deploys it.
Also commits any newly fetched Wikipedia cache entries back to the repo so subsequent
builds don't have to re-fetch them.

### Issue to post (`.github/workflows/issue-to-post.yml`)

Write a post entirely from a GitHub Issue:

1. Create a new issue — use the issue title as the post title and write the post body in Markdown in the issue description.
2. Add any topic labels you want (e.g. `python`, `unix`) — these become the post's tags.
3. Apply the `blog-post` label — this triggers the workflow immediately.

The workflow converts the issue into a Nikola post (preserving the issue's creation date),
commits it to `posts/YYYY/MM/DD/<slug>.md`, and pushes to `master`, which in turn triggers
the publish workflow to build and deploy the site.

> Note: the post is created when the `blog-post` label is **applied**, not when the issue is closed.

### New post (`.github/workflows/new-post.yml`)

Creates a blank post stub via `workflow_dispatch`. Go to Actions → Create New Post, supply
a title and optional comma-separated tags, and a new Markdown file will be committed to
`posts/` ready for editing.

## Wikipedia plugin

Posts support a `wikipedia` shortcode that renders an inline tooltip linking to a Wikipedia article.

```
{{% wikipedia article="Python (programming language)" %}}
{{% wikipedia article="Unix" text="Unix systems" lang="en" %}}
```

| Parameter | Default | Description |
|-----------|---------|-------------|
| `article` | required | Wikipedia page title (as it appears in the URL) |
| `text`    | article name | Link text shown to the reader |
| `lang`    | `en`    | Wikipedia language code |

Fetched summaries are cached in `cache/wikipedia_cache.json` (tracked in git) so Wikipedia
is only contacted for articles not already in the cache. The plugin retries automatically
with exponential backoff if Wikipedia rate-limits the request.

[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/orsenthil/senthil.learntosolveit.com&stack=cms)
