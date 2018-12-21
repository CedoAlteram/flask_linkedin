#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from linkedin_scraper import grab_em

app = Flask(__name__)

#TODO
# This this is clunk AF, but it works.
# Add in more error trapping.


@app.route('/todo/api/v1.0/tasks/<string:company>', methods=['GET'])
def get_task(company):
    # grabs incoming string off request and un-urllifies it.
    un_url_company = company.replace("-", " ")
    url_list = grab_em(un_url_company)
    if len(company) == 0:
        abort(404)
    return jsonify({'company_img_urls': url_list})


if __name__ == '__main__':
    app.run(debug=True)
