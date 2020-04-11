from exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class CMSPermission(object):
    # 255的二进制表示方式 1111 1111
    ALL_PERMISSION = 0b11111111
    # 1.访问者权限
    VISITOR = 0b00000001
    # 2.管理帖子权限
    POSTER = 0b00000010
    # 3.管理评论的权限
    COMMENTER = 0b00000100
    # 4.管理版块的权限
    BOARDR = 0b00001000
    # 5.管理前台用户的权限
    FRONTUSER = 0b00010000
    # 6.管理后台用户的权限
    CMSUSER = 0b00100000
    # 6.管理后台管理员的权限
    admin = 0b01000000


cms_role_user = db.Table(
    'cms_role_user',
    db.Column('cms_role_id', db.Integer, db.ForeignKey('cms_role.id'), primary_key=True),
    db.Column('cms_user_id', db.Integer, db.ForeignKey('cms_user.id'), primary_key=True)
)


class CMSRole(db.Model):
    __tablename__ = 'cms_role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.String(200), nullable=True)
    create_time = db.Column(db.DateTime, default=datetime.now())
    permissions = db.Column(db.Integer, default=CMSPermission.VISITOR)
    users = db.relationship('CMSUser', secondary=cms_role_user, backref='roles')


class CMSUser(db.Model):
    __tablename__ = 'cms_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    _password = db.Column(db.String(100), nullable=False) # 加上_ ,防止和方法名冲突
    email = db.Column(db.String(50), nullable=False, unique=True)
    join_time = db.Column(db.DateTime, default=datetime.now())

    # password名字变化，重写构造函数，使得映射是正常的
    def __init__(self, username, password, email):
        self.username = username
        # 调用的是方法
        self.password = password
        self.email = email

    # 将方法添加@property注解，可以通过访问属性的方式访问方法，print(user.password)
    @property
    def password(self):
        return self._password

    # 可以通过 user.password = 'abc' 这种方式给password赋值
    @password.setter
    def password(self, raw_password):
        # 对密码加密保存
        self._password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        result = check_password_hash(self._password, raw_password)
        return result

    @property
    def permissions(self):
        if not self.roles:
            return 0
        all_permissions = 0
        for role in self.roles:
            permissions = role.permissions
            all_permissions |= permissions
        return all_permissions

    def has_permission(self, permission):
        return self.permissions & permission == permission

    @property
    def is_developer(self):
        return self.has_permission(CMSPermission.ALL_PERMISSION)