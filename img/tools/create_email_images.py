from text_to_image import text_to_image_fitting

email_dict = {
    'David Srolovitz' : 'srol@hku.hk',
    'Subrahmanyam Pattamatta' : 'psmanyam@hku.hk',
    'Tongqi Wen' : 'tongqwen@hku.hk',
    'Zhuoyuan Li' : 'zhuoyuan_li@outlook.com',
    'Zhizi Guan' : 'zhiziguan@connect.hku.hk',
    'Xiaoguo Gong' : 'gongxg@connect.hku.hk',
    'Anwen Liu' : 'anwenliu2-c@my.CityU.edu.hk',
    'Jinxin Yu' : 'jinxinyu2-c@my.cityu.edu',
    'Jing Fang' : 'jingfang9-c@my.cityu.edu.hk',
    'Zhaowei Wang': 'zhaowwang2-c@my.cityu.edu.hk',
    'Dongsong Tao': 'dongsotao2-c@my.cityu.edu.hk',
    'Caihao Qiu' : 'caihaoqiu2-c@my.cityu.edu.hk',
    'Siqi Wang' : 'swang347-c@my.cityu.edu.hk',
    'Avatar X' : 'avatarX@abc.edu'
}

for name, email in email_dict.items():

    filename = name.lower()
    filename = '../group/emails/' + filename.replace(' ', '_') + '.png'
    text_to_image_fitting(email, filename)