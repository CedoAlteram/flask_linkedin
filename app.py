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

    # url_list = [
    #     'https://media.licdn.com/dms/image/C4E03AQGfOILBVqRE4A/profile-displayphoto-shrink_800_800/0?e=1550707200&v=beta&t=0q7kExCOhn3PafGut-YBGhasboneKM36d2YrsEehULE',
    #     'https://media.licdn.com/dms/image/C5603AQG3ik4TSBqxPw/profile-displayphoto-shrink_100_100/0?e=1550707200&v=beta&t=HHJtYH5K2qDDoNbTg9rF92toGlVVG7RTygQ7eB0fQOI',
    #     'https://media.licdn.com/dms/image/C5603AQHltlS189VbyA/profile-displayphoto-shrink_800_800/0?e=1550707200&v=beta&t=wjnUaBOhV4ibUdPjwbWBTvyXZsqC9_AGhqnSCKkOWMk',
    #     'https://media.licdn.com/dms/image/C5603AQGyVpS9uxyqYA/profile-displayphoto-shrink_800_800/0?e=1550707200&v=beta&t=uaLzOxVD4N9to3c7Ca4apqdj45s4NqmAR51Hy5D4TAg',
    #     'https://media.licdn.com/dms/image/C5103AQH1ikLbibZAeA/profile-displayphoto-shrink_800_800/0?e=1550707200&v=beta&t=mcDpV5ytcotCXS-_bLSP9JDN0SAsMDk22nH_X8YF-2Y',
    #     'https://media.licdn.com/dms/image/C4D03AQEJXw4jN-8BgQ/profile-displayphoto-shrink_800_800/0?e=1550707200&v=beta&t=Ee-uCY2_uh_emKghelxutM0aQLEPj-kBy9KxJfacucU',
    #     'https://media.licdn.com/dms/image/C5603AQG3ik4TSBqxPw/profile-displayphoto-shrink_100_100/0?e=1550707200&v=beta&t=HHJtYH5K2qDDoNbTg9rF92toGlVVG7RTygQ7eB0fQOI',
    #     'https://media.licdn.com/dms/image/C5603AQEwN-qZecqQvw/profile-displayphoto-shrink_800_800/0?e=1550707200&v=beta&t=aEOwhLNXWSOH7PSdBVKDX5ORkP7iXb8Qzzw3iUmPS18',
    #     'https://media.licdn.com/dms/image/C5603AQFRT38-zp5uyQ/profile-displayphoto-shrink_800_800/0?e=1550707200&v=beta&t=6YOL-j5B4oMRqxNcy0vLeh2sitQVaWJvQ-tzC8wgM60',
    #     'https://media.licdn.com/dms/image/C5603AQG87Lai2h_qYg/profile-displayphoto-shrink_800_800/0?e=1550707200&v=beta&t=NXfqPxAwzO11TpHqdchlNY5kdIg6TVQu29suXyZpaqA',
    #     'https://media.licdn.com/dms/image/C4E03AQEpA62pXbNqog/profile-displayphoto-shrink_800_800/0?e=1550707200&v=beta&t=E9_mxlI0PfT5WWnF71KQFwZLyRHuMLcQbD9UlqZCMhc',
    #     'https://media.licdn.com/dms/image/C5603AQG3ik4TSBqxPw/profile-displayphoto-shrink_100_100/0?e=1550707200&v=beta&t=HHJtYH5K2qDDoNbTg9rF92toGlVVG7RTygQ7eB0fQOI',
    #     'https://media.licdn.com/dms/image/C5103AQHuBSlhvfV1mQ/profile-displayphoto-shrink_800_800/0?e=1550707200&v=beta&t=j0RDwVQe_lLPDMnXci0rAmPs9gGtOX4ixytUYmYRF5Y',
    #     'https://media.licdn.com/dms/image/C5603AQEewzgvlwpraA/profile-displayphoto-shrink_800_800/0?e=1550707200&v=beta&t=EDmfClhL_ugTH9rDd4NzIw9C4yACJXP-XIULxegBb-k',
    #     'https://media.licdn.com/dms/image/C5603AQGXAggAY74u3Q/profile-displayphoto-shrink_800_800/0?e=1550707200&v=beta&t=BKJnWZdj2o3o4d_JMA9ORIKdjZmLi3Ah4sxE-KX1_EQ',
    #     'https://media.licdn.com/dms/image/C4E03AQEqx_92-pobxQ/profile-displayphoto-shrink_800_800/0?e=1550707200&v=beta&t=eUfJZqQhYakw0jBGDao-sD0yqijhlcl_8ozcQApo9cI',
    #     'https://media.licdn.com/dms/image/C5603AQG3ik4TSBqxPw/profile-displayphoto-shrink_100_100/0?e=1550707200&v=beta&t=HHJtYH5K2qDDoNbTg9rF92toGlVVG7RTygQ7eB0fQOI']

    un_url_company = company.replace("-", " ")
    url_list = grab_em(un_url_company)
    print(un_url_company, 'this is un_url_company')
    # simple test to see if functionality of API is returning values.
    if len(company) == 0:
        abort(404)
    return jsonify({'company_img_urls': url_list})


if __name__ == '__main__':
    app.run(debug=True)
