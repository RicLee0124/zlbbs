from .views import bp
import config
from flask import session, g
from .models import CMSUser, CMSPermission


@bp.before_request
def before_request():
    if config.CMS_USER_ID in session:
        user_id = session.get(config.CMS_USER_ID)
        user = CMSUser.query.get(user_id)
        if user:
            g.cms_user = user


# 只要是在bp蓝图中处理的模板 都可以使用这个CMSPermission对象
@bp.context_processor
def cms_context_processor():
    return {"CMSPermission": CMSPermission}
