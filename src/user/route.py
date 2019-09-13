from flask import Flask, request,jsonify

from .controller import  updateUser


def apiLogin(app):
    @app.route('/user/<string:userId>', methods=['GET','POST'])
    def login(userId):
        # 请求user
        if(request.method=="POST"):
            return jsonify({
                "userId":userId,
                "name":'swq',
                "job":'web',
            })
        # 更新用户
        else:
            return  updateUser(userId,request.form)

    return login



