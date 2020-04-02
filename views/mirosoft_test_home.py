# @File: microsoft_test_home
# @Author: Kevin Huo
# @LastUpdate: 4/2/2020 11:13 AM


from flask import render_template, make_response


def msft_test_home_func():
    """
    microsoft test home page
    source - https://github.com/microsoft/python-sample-vscode-flask-tutorial/blob/master/hello_app/static/site.css
    """
    html = render_template("microsoft_layout.html")

    res = make_response(html)
    res.status_code = 200
    return res
