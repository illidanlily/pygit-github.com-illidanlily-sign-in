import random
import numpy as np
import csv
import os


def random_information():  # 随机生成信息
    # 百家姓姓氏
    firstName = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹窦章云苏潘葛范彭郎鲁韦昌马苗凤花方俞任袁柳鲍史唐"
    # 百家姓中双姓氏
    firstName2 = "万俟司马上官欧阳夏侯诸葛东方皇甫尉迟理塘"
    # 女孩名字
    girl = '秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲真环雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼勤珍贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑婕馨瑗琰韵融园艺咏卿聪澜纯毓悦昭冰爽琬茗羽希宁欣飘育滢馥筠柔竹霭凝晓欢霄枫芸菲寒伊亚宜可姬舒影荔枝思丽'
    # 男孩名字
    boy = '丁伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国胜学祥才发武新利清飞彬富顺信子杰涛昌成康星光天达安岩中茂进林有坚和彪博诚先敬震振壮会思群豪心邦承乐绍功松善厚庆磊民友裕河哲江超浩亮政谦亨奇固之轮翰朗伯宏言若鸣朋斌梁栋维启克伦翔旭鹏泽晨辰士以建家致树炎德行时泰盛雄琛钧冠策腾楠榕风航弘'
    # 名
    name = '真中凯歌易仁器义礼智信友'

    # 10%的机遇生成双数姓氏
    if random.choice(range(100)) > 10:
        firstName_name = firstName[random.choice(range(len(firstName)))]
    else:
        i = random.choice(range(len(firstName2)))
        if i//2==0:
            i+=1
        firstName_name = firstName2[i:i + 2]

    sex = random.choice(range(2))

    age = random.choice(range(20,23))

    grade = random.choice(np.random.normal(3, 1, 1))
    while grade>4 or grade<1.5:
        grade = random.choice(np.random.normal(3, 1, 1))
    name_1 = ""
    flagg=0
    if random.choice(range(2)) > 0:
        name_1 = name[random.choice(range(len(name)))]

    if random.choice(range(100))<7:
        flagg=1
    a = []
    if flagg == 1:
        for x in range(20):
            tmp = random.choice(range(100))
            if tmp < 80:
                a.append(str(0))
            else:
                a.append(str(1))
    else:
        for x in range(20):
            tmp = random.choice(range(100))
            if tmp > 95:
                a.append(str(0))
            else:
                a.append(str(1))

    # 生成并返回一个名字
    if sex > 0:
        girl_name = girl[random.choice(range(len(girl)))]
        information = firstName_name + name_1 + girl_name + "," + '女' + ',' + str(age) + ',' + str(round(grade,3))+','+a[0]+','+a[1]+','+a[2]+','+a[3]+','+a[4]+','+a[5]+','+a[6]+','+a[7]+','+a[8]+','+a[9]+','+a[10]+','+a[11]+','+a[12]+','+a[13]+','+a[14]+','+a[15]+','+a[16]+','+a[17]+','+a[18]+','+a[19]+','+'50'
    else:
        boy_name = boy[random.choice(range(len(boy)))]
        if random.choice(range(2)) > 0:
            name_1 = name[random.choice(range(len(name)))]
        information = firstName_name + name_1 + boy_name + ',' + '男' + ','+  str(age) + ',' + str(round(grade,3))+','+a[0]+','+a[1]+','+a[2]+','+a[3]+','+a[4]+','+a[5]+','+a[6]+','+a[7]+','+a[8]+','+a[9]+','+a[10]+','+a[11]+','+a[12]+','+a[13]+','+a[14]+','+a[15]+','+a[16]+','+a[17]+','+a[18]+','+a[19]+','+'50'
    return information


def main():
    with open('D:\\软件工程.csv', 'w') as m:
        msg1 = '姓名' +','+ '性别' +','+ '年龄' +','+ '绩点' +','+ '出勤1'+',' + '出勤2'+',' + '出勤3'+',' + '出勤4'+',' + '出勤5' +','+ '出勤6' +','+ '出勤7' +','+ '出勤8'+',' + '出勤9'+',' + '出勤10' +','+ '出勤11' +','+ '出勤12'+',' + '出勤13'+',' + '出勤14'+',' + '出勤15' +','+ '出勤16' +','+ '出勤17'+',' + '出勤18' +','+ '出勤19'+','+'出勤20'+','+'概率'
        m.write('{}\n'.format(msg1))
        for i in range(N):
            msg = random_information()
            m.write('{}\n'.format(msg))
    with open('D:\\概率论.csv', 'w') as m:
        msg1 = '姓名' + ',' + '性别' + ',' + '年龄' + ',' + '绩点' + ',' + '出勤1' + ',' + '出勤2' + ',' + '出勤3' + ',' + '出勤4' + ',' + '出勤5' + ',' + '出勤6' + ',' + '出勤7' + ',' + '出勤8' + ',' + '出勤9' + ',' + '出勤10' + ',' + '出勤11' + ',' + '出勤12' + ',' + '出勤13' + ',' + '出勤14' + ',' + '出勤15' + ',' + '出勤16' + ',' + '出勤17' + ',' + '出勤18' + ',' + '出勤19' + ',' + '出勤20' + ',' + '概率'
        m.write('{}\n'.format(msg1))
        for i in range(N):
            msg = random_information()
            m.write('{}\n'.format(msg))
    with open('D:\\数据库.csv', 'w') as m:
        msg1 = '姓名' +','+ '性别' +','+ '年龄' +','+ '绩点' +','+ '出勤1'+',' + '出勤2'+',' + '出勤3'+',' + '出勤4'+',' + '出勤5' +','+ '出勤6' +','+ '出勤7' +','+ '出勤8'+',' + '出勤9'+',' + '出勤10' +','+ '出勤11' +','+ '出勤12'+',' + '出勤13'+',' + '出勤14'+',' + '出勤15' +','+ '出勤16' +','+ '出勤17'+',' + '出勤18' +','+ '出勤19'+','+'出勤20'+','+'概率'
        m.write('{}\n'.format(msg1))
        for i in range(N):
            msg = random_information()
            m.write('{}\n'.format(msg))
    with open('D:\\图形学.csv', 'w') as m:
        msg1 = '姓名' +','+ '性别' +','+ '年龄' +','+ '绩点' +','+ '出勤1'+',' + '出勤2'+',' + '出勤3'+',' + '出勤4'+',' + '出勤5' +','+ '出勤6' +','+ '出勤7' +','+ '出勤8'+',' + '出勤9'+',' + '出勤10' +','+ '出勤11' +','+ '出勤12'+',' + '出勤13'+',' + '出勤14'+',' + '出勤15' +','+ '出勤16' +','+ '出勤17'+',' + '出勤18' +','+ '出勤19'+','+'出勤20'+','+'概率'
        m.write('{}\n'.format(msg1))
        for i in range(N):
            msg = random_information()
            m.write('{}\n'.format(msg))
    with open('D:\\接口技术.csv', 'w') as m:
        msg1 = '姓名' +','+ '性别' +','+ '年龄' +','+ '绩点' +','+ '出勤1'+',' + '出勤2'+',' + '出勤3'+',' + '出勤4'+',' + '出勤5' +','+ '出勤6' +','+ '出勤7' +','+ '出勤8'+',' + '出勤9'+',' + '出勤10' +','+ '出勤11' +','+ '出勤12'+',' + '出勤13'+',' + '出勤14'+',' + '出勤15' +','+ '出勤16' +','+ '出勤17'+',' + '出勤18' +','+ '出勤19'+','+'出勤20'+','+'概率'
        m.write('{}\n'.format(msg1))
        for i in range(N):
            msg = random_information()
            m.write('{}\n'.format(msg))

N = 90
main()