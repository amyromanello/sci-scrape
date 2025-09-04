from jinja2 import Template
from datetime import datetime


def render_jobs_email(user_name, jobs):
    current_date = datetime.now().strftime("%B %d, %Y")

    template_str = """<html>
    <body style="font-family: 'Helvetica', Arial, sans-serif; line-height:1.5; background-color:#f9f9f9; padding:20px;">
    <div style="max-width:600px; margin:auto; background-color:white; border-radius:10px; box-shadow:0 0 10px rgba(0,0,0,0.1); padding:30px;">
      <h2 style="color:#004080;">👋 Hi {{ user_name }}!</h2>
      <p>It's me, <strong>Amy</strong>...bringing you today's hottest jobs, locally sourced with <span style="color:#ff6600;">SciScrape</span>! 🚀</p>
      <p>Here's what's new as of <strong>{{ current_date }}</strong>:</p>

      {% for job in jobs %}
        <div style="border-bottom:1px solid #eee; padding:15px 0;">
          <h3 style="margin:0; color:#0066cc;">
            <a href="{{ job.link }}" style="text-decoration:none; color:#0066cc;">{{ job.title }} 🔗</a>
          </h3>
          <p style="margin:5px 0 0 0; color:#555;">🏢 {{ job.institution }}</p>
          <p style="margin:2px 0 0 0; color:#999;">📅 Posted on {{ job.date }}</p>
        </div>
      {% endfor %}

      <p style="margin-top:20px; color:#888;">Keep an eye out, more jobs are coming soon! ✨</p>
    </div>
    </body>
    </html>"""

    return Template(template_str).render(user_name=user_name, jobs=jobs, current_date=current_date)
