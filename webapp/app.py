import talisker.requests

# Packages
from canonicalwebteam.flask_base.app import FlaskBase
from canonicalwebteam import image_template
from canonicalwebteam.discourse import DiscourseAPI, DocParser, Docs

from flask import render_template, make_response

from webapp.tutorials.views import init_tutorials

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
        index_topic_id=3749,
        url_prefix="/docs",
    ),
    document_template="docs/document.html",
    url_prefix="/docs",
    blueprint_name="main_docs",
)
main_docs.init_app(app)

init_tutorials(app, "/tutorials")


@app.context_processor
def utility_processor():
    return {"image": image_template}


@app.route("/")
def index_temp():
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


@app.route("/sitemap.xml")
def sitemap_index():
    xml_sitemap = render_template("sitemap/sitemap-index.xml")
    response = make_response(xml_sitemap)
    response.headers["Content-Type"] = "application/xml"

    return response


@app.route("/sitemap-links.xml")
def sitemap_links():
    xml_sitemap = render_template("sitemap/sitemap-links.xml")
    response = make_response(xml_sitemap)
    response.headers["Content-Type"] = "application/xml"

    return response
