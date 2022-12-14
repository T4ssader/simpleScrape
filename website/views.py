from flask import Blueprint, render_template, request
from .models import Scrape
from flask_login import login_required, current_user
from . import db

views = Blueprint("views", __name__)


@views.route("/")
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route("/scrape", methods=['GET', 'POST'])
@login_required
def scrape():
    if request.method == "POST":
        scraping_regex = request.form.get("regex")
        scraping_url = request.form.get("url")

        new_scraping_request = Scrape(url=scraping_url, regex=scraping_regex)
        db.session.add(new_scraping_request)
        db.session.commit()
    else:
        return render_template("scraping.html", user=current_user)
