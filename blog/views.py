# -*- coding: UTF-8 -*-
from django.http import HttpResponse, HttpRequest, QueryDict
import urllib, json, sys
import vk

def post_list(request):
    if 'has_commented' in request.session:
        uid = request.GET['uid']
        session = vk.Session()
        api = vk.API(session)
        user = api.users.get(user_ids=int(uid),)
        friends = api.friends.get(user_id=int(uid), order="random", count=5, fields ={"first_name", "last_name"})
        request.GET['first_name'].encode("utf-8"), request.GET['last_name'].encode("utf-8")
        def max_user():
            result = ""
            for user in friends:
                 result += "<p><a href='https://vk.com/id%s'>%s %s</a></p>" % (user[u'user_id'], user[u'first_name'].encode("utf-8"), user[u'last_name'].encode("utf-8"))
            return result

        head = "<html>\
                    <head>\
                        <title>Document</title>\
                    </head>\
                    <body>\
                        <h1>Здравствуйте, {0} {1}!</h1>\
                        <div>\
                            <p>ваши друзья соскучились за вами:</p>\
                            {2}\
                            <p>скорее свяжитесь с ними</p>\
                        <div>\
                    </body>\
                    </html>"

        return HttpResponse(head. format(request.GET['first_name'].encode("utf-8"), request.GET['last_name'].encode("utf-8"), max_user()))


    head = "<html>\
                <head>\
                    <script src="'https://vk.com/js/api/openapi.js?139'" type="'text/javascript'"></script>\
                    <title>Document</title>\
                </head>\
                <body>\
                    <script type='text/javascript'>\
                        VK.init({\
                        apiId: 12345\
                        });\
                    </script>\
                    <div id='vk_auth'></div>\
                    <script type='text/javascript'>\
                        VK.Widgets.Auth('vk_auth', {});\
                    </script>\
                </body>\
            </html>"
    request.session['has_commented'] = "true"
    return HttpResponse(head)
