from django import forms

# 定义一个类 => 一个表单
class ContactForm(forms.Form):
    # 一个属性就是一个表单元素
    # forms.CharFiled => 字段类型

    # label => 参数
    """
        label => 设置标题（默认：属性名）
        required => True (默认必填项)
        min_length => 设置内容的最短长度
        initial => 初始化的值
        error_messages => 设置错误提示信息 => 后端验证errors信息
    """
    # widgets => 小部件
    subject = forms.CharField(label="主题",
                              min_length = 8,
                              required=True,
                              # initial="Django-Form",
                              error_messages={
                                  "min_length":"主题最少为8字符",
                                  "required":"主题是必填项",
                              }
                              )
    content = forms.CharField(label="正文",
                              widget=forms.Textarea)
    content2 = forms.CharField(label="正文2",
                               widget=forms.Textarea(
                                   attrs={"name":"content2",
                                          "class":"clasa",
                                          "style":"color:red;font-size:20px;",
                                          "cols": 20,
                                         }
                                       )
                               )
    sender = forms.EmailField(label="发送人")
    cc_myself = forms.BooleanField(label="抄送")
    # 密码字段
    password = forms.CharField(label="密码", widget=forms.PasswordInput)
    # 单radio值为字符串
    gender = forms.fields.ChoiceField(
        choices=((1, "男"), (2, "女"), (3, "保密")),
        label="性别",
        initial=3,
        widget=forms.widgets.RadioSelect()
    )
    # 下拉选择
    hobby = forms.fields.ChoiceField(
        choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
        label="爱好",
        initial=3,
        widget=forms.widgets.Select()
    )
    #  多选
    hobby2 = forms.fields.MultipleChoiceField(
        choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
        label="爱好",
        initial=[1, 3],
        widget=forms.widgets.SelectMultiple()
    )
    # 单选checkbox
    keep = forms.fields.ChoiceField(
        label="是否记住密码",
        initial="checked",
        widget=forms.widgets.CheckboxInput()
    )
    # 多选checkbox
    hobby3 = forms.fields.MultipleChoiceField(
        choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
        label="爱好",
        initial=[1, 3],
        widget=forms.widgets.CheckboxSelectMultiple()
    )



# 通过django.forms定义表单
from django import forms
from . import models


class RegisterForm(forms.ModelForm):
    """注册表单"""
    # 因为Model中的元素默认是会把密码显示出来的，所以在这里重新定义一个password
    password = forms.CharField(label="输入密码", max_length=18, widget=forms.PasswordInput)
    password2 = forms.CharField(label="确认密码", max_length=18, widget=forms.PasswordInput)
    class Meta:
        model = models.UserInfo
        # 将model UserInfo中的字段生成到表单
        # exclude表示排除哪个字段，fields表示包含哪个字段， 两个选项必须选其一
        # exclude = ()
        fields = ('username', 'password')

    def clean_username(self):
        """
        对username字段做检查用户名是否已经被注册
        注意字段一定要有返回值
        """
        # self.cleaned_data["username"] => 获取表单提交的username数据
        users = models.UserInfo.objects.filter(username=self.cleaned_data["username"])
        if not users:
            return self.cleaned_data["username"]
        else:
            raise forms.ValidationError("该用户名已经被使用")

    def clean(self):
        """
        验证两次输入的密码是否一次
        对整个表单验证时，不需要返回值
        """
        # if self.cleaned_data["password"] != self.cleaned_data["password2"]:
        #     raise forms.ValidationError("密码不一致！")
        if self.cleaned_data.get("password") and self.cleaned_data.get("password") != self.cleaned_data.get("password2"):
            raise forms.ValidationError("密码不一致！")
        return self.cleaned_data


class LoginForm(forms.ModelForm):
    """登录表单"""
    password = forms.CharField(label="密码", max_length=30, widget=forms.PasswordInput(attrs={"size": 20, }))

    def clean_username(self):
        user = models.UserInfo.objects.filter(username__iexact=self.cleaned_data["username"])
        if not user:
            raise forms.ValidationError("用户不存在")
        else:
            return self.cleaned_data["username"].lower()

    class Meta:
        # 配置用
        model = models.UserInfo   # 对应的Model中的类
        exclude = ()
        # fields = (field1, field2)  # 字段，如果是__all__,就是表示列出所有的字段
        # labels = None  # 提示信息
        # help_texts = None  # 帮助提示信息
        # widgets = None  # 自定义插件
        # error_messages = None  # 自定义错误信息