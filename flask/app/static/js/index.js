// 字符串占位符拼接方法
// var str3 = "史上第一个30000+8000+8000球员：{name}, 性别{sex}, 今年{age}岁".signMix(user);
// 史上第一个30000+8000+8000球员：James, 性别male, 今年34岁
String.prototype.signMix = function () {
    if (arguments.length === 0) return this;
    var param = arguments[0], str = this;
    if (typeof (param) === 'object') {
        for (var key in param)
            str = str.replace(new RegExp("\\{" + key + "\\}", "g"), param[key]);
        return str;
    } else {
        for (var i = 0; i < arguments.length; i++)
            str = str.replace(new RegExp("\\{" + i + "\\}", "g"), arguments[i]);
        return str;
    }
};

function toastr_pd(e, type) {
    if (e === 'success') {
        toastr.success(type + '成功');
    } else {
        toastr.error(type + '失败')
    }
}