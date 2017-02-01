"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request
import json



swear_words=["anal","anus","arse","ass","ballsack","balls","bastard","bitch","biatch","bloody","blowjob","blow job","bollock","bollok","boner","boob","bugger","bum","butt","buttplug","clitoris","cock","coon","crap","cunt","damn","dick","dildo","dyke","fag","feck","fellate","fellatio","felching","fuck","f u c k","fudgepacker","fudge packer","flange","Goddamn","God damn","hell","homo","jerk","jizz","knobend","knob end","labia","lmao","lmfao","muff","nigger","nigga","omg","penis","piss","poop","prick","pube","pussy","queer","scrotum","sex","shit","shit","sh1t","slut","smegma","spunk","tit","tosser","turd","twat","vagina","wank","whore","wtf"]
love_words=["love","like","enjoy"]
hate_words=["don't","doesn't","hate","hates"]
yes_words=["yes","yeah","y","yess"]
no_words=["no","non","n"]
great_words=["well","fine","good","happy","perfect","excited"]
hello_words=["hello","hi"]


def swear(list):
    return any(x in list for x in swear_words)

def question(list):
    if list[-1]=="?":
        return True
    return False

def love(list):
    return any(x in list for x in love_words)

def hate(list):
    return any(x in list for x in hate_words)

def yes(list):
    return any(x in list for x in yes_words)

def no(list):
    return any(x in list for x in no_words)

def great(list):
    return any(x in list for x in great_words)

def hello(list):
    return any(x in list for x in hello_words)

@route('/', method='GET')
def index():
    return template("chatbot.html")


@route('/chat', method='POST')
def chat():
    user_message = request.POST.get('msg')
    new_list = user_message.split(" ")
    if hello(new_list):
        return json.dumps({"animation": "confused", "msg": "Nice to meet you"})
    if swear(new_list):
        return json.dumps({"animation": "afraid", "msg": "Don't say swear words please"})

    if question(new_list):
        if love(new_list):
            return json.dumps({"animation": "in love", "msg": "Yes, and you ?"})

        else:
            return json.dumps({"animation": "laughing", "msg": "I don't know, sorry ..."})

    if love(new_list):
        return json.dumps({"animation": "dancing", "msg": "me too"})

    if hate(new_list):
        return json.dumps({"animation": "heartbroke", "msg": "me too "})
    if yes(new_list):
        return json.dumps({"animation": "excited", "msg": "We like same things!!"})
    if no(new_list):
        return json.dumps({"animation": "no", "msg": "Me neither"})
    if "I" in new_list and great(new_list):
        return json.dumps({"animation": "giggling", "msg": "Good to hear that !"})
    else:
        return json.dumps({"animation": "ok", "msg": "Ok"})


@route('/test', method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7007)

if __name__ == '__main__':
    main()
