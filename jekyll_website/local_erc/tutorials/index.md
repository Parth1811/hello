---
layout: page
title: Tutorials
excerpt: "Learn at your own pace!"
search_omit: true
paginate: true
paginate:
  collection:   posts
  per_page:     6
  limit:        false
  categories:   [tutorials]
---

<ul class="post-list">
    {% for tut in paginator.posts %}
    <li><article><a href="{{ site.url }}{{ tut.permalink }}">{{ tut.title }}
        <span class="excerpt">{% if tut.excerpt %}{{ tut.excerpt | remove: '\[ ... \]' | remove: '\( ... \)' | markdownify | strip_html | strip_newlines | escape_once }}{% endif %}<br>{% if tut.contributors %}Contributor(s): {{ tut.contributors }}{% endif %}</span>
    </a></article></li>
    {% endfor %}
</ul>

<!-- Pagination links -->
<div class="pagination">
  {% if paginator.previous_page %}
    <a href="{{ site.url }}{{ paginator.previous_page_path }}" class="previous btn">Previous</a>
  {% endif %}
  <span class="page_number btn2" align="justify">Page: {{ paginator.page }} of {{ paginator.total_pages }}</span>
  {% if paginator.next_page %}
    <a href="{{ site.url }}{{ paginator.next_page_path }}" class="next btn">Next</a>
  {% endif %}
</div>
