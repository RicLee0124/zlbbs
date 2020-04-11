from .views import bp
# 在执行init时需要导入hooks，不然钩子函数不会被执行
import apps.cms.hooks
