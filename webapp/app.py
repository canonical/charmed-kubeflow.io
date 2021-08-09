import talisker.requests

# Packages
from canonicalwebteam.flask_base.app import FlaskBase
from canonicalwebteam import image_template
from canonicalwebteam.discourse import DiscourseAPI, DocParser, Docs

from flask import render_template

# Rename your project below
app = FlaskBase(
    __name__,
    "charmed-kubeflow.io",
    template_folder="../templates",
    static_folder="../static",
    template_404="404.html",
    template_500="500.html",
)
session = talisker.requests.get_session()

main_docs = Docs(
    parser=DocParser(
        api=DiscourseAPI(
            base_url="https://discourse.charmhub.io/", session=session
        ),
        index_topic_id=4943,
        url_prefix="/docs",
    ),
    document_template="docs/document.html",
    url_prefix="/docs",
    blueprint_name="main_docs",
)
main_docs.init_app(app)


@app.context_processor
def utility_processor():
    return {"image": image_template}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/thank-you")
def thank_you():
    return render_template("thank-you.html")


@app.route("/contact-us")
def contact_us():
    return render_template("contact-us.html")


@app.route("/includes/contact-us")
def includes_contact_us():
    return render_template("includes/contact-us.html")
