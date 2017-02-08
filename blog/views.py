# -*- coding: UTF-8 -*-
from django.http import HttpResponse
import vk

def max_user(friends):
    result = ""
    for user in friends:
        result += "<p><a href='https://vk.com/id%s'>%s %s</a></p>\n" % (user[u'user_id'], user[u'first_name'].encode("utf-8"), user[u'last_name'].encode("utf-8"))
    return result

def post_list(request):
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
            VK.Widgets.Auth('vk_auth',{});\
            </script>\
            </body>\
            </html>"

    if 'uid' in request.GET:
        request.session["uid"] = request.GET["uid"]

    if "uid" in request.session:
        uid = request.session["uid"]
        session = vk.Session()
        api = vk.API(session)
        user = api.users.get(user_ids=int(uid))
        friends = api.friends.get(user_id=int(uid), order="random", count=5,\
                                  fields ={"first_name", "last_name"})
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

        return HttpResponse(head.format(user[0]['first_name'].encode("utf-8"), \
                                        user[0]['last_name'].encode("utf-8"),\
                                        max_user(friends)))
    return HttpResponse(head)
