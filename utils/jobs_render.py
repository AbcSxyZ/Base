import json
from pathlib import Path

JOBS_LOCATION = Path("jobs/offers")

TEMPLATE = """---
title: "{title}"
author: "{organization}"
date: {date_posted}
categories: {categories}
description: "{resume}"
---

```{{=html}}
<script type="application/ld+json">
{raw_json}
</script>
```

**See job offer: <{url}>**

{description}
"""

def render_job(job_path):
    """Create Markdown file for a job offer based on JSON-LD data"""
    destination = job_path.with_suffix(".md")
    data = json.loads(job_path.read_text())

    job_info = {
        "title": data["title"],
        "date_posted": data["datePosted"],
        "categories": data["occupationalCategory"],
        "resume": data["resume"].replace('"', '\\"'),
        "description": data["description"],
        "organization": data["hiringOrganization"]["name"],
        "url": data["url"],
        "raw_json": json.dumps(data, indent=2, ensure_ascii=False),
            }

    publication = TEMPLATE.format(**job_info)
    destination.write_text(publication)

if __name__ == "__main__":
    jobs_list = JOBS_LOCATION.glob("*.json")

    for job in jobs_list:
        render_job(job)
