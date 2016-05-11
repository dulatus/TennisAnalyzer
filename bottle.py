# -*- coding: utf-8 -*-
"""
Created on Mon May  9 14:47:49 2016

@author: Daniyar_Amangeldy
"""

from bottle import run,request,template,static_file

app = Bottle()


@app.route('/')
@app.route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)






@app.route('/hello')
def hello():
    return '''
    <head>
    <title>Tennis Analyzer</title>
    <link rel="icon" href="http://pngimg.com/upload/tennis_PNG10405.png">
  </head>
    <body>
     <form action="/hello" method="post" class="forms">
            </br> <input name="player1" type="text" placeholder="Player 1" id="pl1" />
             <input name="player2" type="text" placeholder="Player 2"  id="pl2" />
            <input value="PREDICT" type="submit" id="submitButton" />
        </form>


    </body>
    <style>
body {
    background-image: url(http://thecourtstore.com/img/cms/linesfinished.jpg);
    background-repeat: no-repeat;
    background-size: cover;

}
#pl1{
margin-top: 325px;
margin-left: 220px;
}
#pl2{
margin-left: 900px;
margin-top: -20px;
}
#submitButton{
margin-top: 100px;
margin-left: -450px;
}

.forms input{
float:left;
border: 1px solid #cccccc;
   border-radius: 3px;
   -webkit-border-radius: 3px;
   -moz-border-radius: 3px;
   -khtml-border-radius: 3px;
   background: #ffffff;
   outline: none;
   height: 24px;
   width: 120px;
   color: #4d4d4d;
   font-size: 11px;
   font-family: Tahoma;

}


</style>
    '''





@app.route('/hello',method='POST')
def result():
    player1 = request.forms.get('player1')
    player2 = request.forms.get('player2')
    return template('''

    <p><head>
    <title>Tennis Analyzer</title>
    <link rel="icon" href="http://pngimg.com/upload/tennis_PNG10405.png">
  </head>
    <body>
     <form action="/hello" method="post" class="forms">
            </br> <input name="player1" type="text" placeholder="{{p1}}" id="pl1" />
             <input name="player2" type="text" placeholder="{{p2}}"  id="pl2" />
            <input value="PREDICT" type="submit" id="submitButton" />
        </form>


    </body>
    <style>
body {
    background-image: url(http://thecourtstore.com/img/cms/linesfinished.jpg);
    background-repeat: no-repeat;
    background-size: cover;

}
#pl1{
margin-top: 325px;
margin-left: 220px;
}
#pl2{
margin-left: 900px;
margin-top: -20px;
}
#submitButton{
margin-top: 100px;
margin-left: -450px;
}

.forms input{
float:left;
border: 1px solid #cccccc;
   border-radius: 3px;
   -webkit-border-radius: 3px;
   -moz-border-radius: 3px;
   -khtml-border-radius: 3px;
   background: #ffffff;
   outline: none;
   height: 24px;
   width: 120px;
   color: #4d4d4d;
   font-size: 11px;
   font-family: Tahoma;

}


</style>
    ''',p1=player1,p2=player2);



run(app, host='localhost', port=8910)
