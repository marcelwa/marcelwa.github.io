---
layout: archive
title: "Conference and Journal Publications"
permalink: /publications/
author_profile: true
---

You can also find my articles on <a href="https://scholar.google.de/citations?user=8wD80wMAAAAJ&hl=en">my Google Scholar profile</a>.

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
