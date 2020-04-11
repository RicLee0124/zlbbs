from flask import Blueprint, request, make_response, jsonify
from utils import restful
from .forms import SMSCaptchaForm
from utils import zlcache
from utils.captcha import Captcha
from io import BytesIO
import qiniu
from tasks import send_sms_captcha

bp = Blueprint("common", __name__, url_prefix='/c')


@bp.route('/sms_captcha/', methods=['POST'])
def sms_captcha():
    form = SMSCaptchaForm(request.form)
    if form.validate():
        telephone = form.telephone.data
        captcha = Captcha.gene_text(number=4)
        send_sms_captcha(telephone, captcha)
        zlcache.set(telephone, captcha)
        return restful.success()
    else:
        return restful.params_error(message='参数错误！')


# http://127.0.0.1:8000/captcha/
@bp.route("/captcha/")
def graph_captcha():
    text, image = Captcha.gene_graph_captcha()
    zlcache.set(text.lower(), text.lower())
    out = BytesIO() # 将文件流放入内存中
    image.save(out, 'png')
    out.seek(0)
    resp = make_response(out.read())
    resp.content_type = 'image/png'
    return resp


@bp.route('/uptoken/')
def uptoken():
    access_key = "JJ-EN789DDyiZjd66VVT7K8BMT1p7DfWaOadBb4z"
    secret_key = "F5UMffWvuEYAbr5p3eW_Nn5XaEAc5AQC97t-LSCz"
    q = qiniu.Auth(access_key, secret_key)

    bucket = "pictureforric2"
    token = q.upload_token(bucket)
    return jsonify({'uptoken': token})

