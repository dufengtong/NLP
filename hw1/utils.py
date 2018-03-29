import copy

standard_words=["近些年", "来","，","快递","行业","发生","了","巨大","转变","，","各类","机器人","正","试图","夺走","快递","小哥","的","工作","。","继","多家","公司","试验","无人机","送货","后","，","地面送货机器人","也","开始","上路","了","。","本月","月初","，","弗吉尼亚州","通过","法案","，","允许","地面送货机器人","上路","，","今天","爱达荷州","（","位于","美国","西北部","）","则","成了","第二个","批准","送货机器人","上路","的","州","，","不过","这项","法案","今年","7","月","1","日","才会","正式","生效","。"]

def calculate_PRF(cut_result_words, standard_words):
    correct_words = []
    temp = copy.copy(standard_words)
    for w in cut_result_words:
        if w in temp:
            correct_words.append(w)
            temp.pop(temp.index(w))
    p = len(correct_words) / len(cut_result_words)
    r = len(correct_words) / len(standard_words)
    f = 2*p*r / (p+r)
    print('cut words:%s\n'%str(cut_result_words))
    print('standard words:%s\n'%str(standard_words))
    print('P:%f R:%f F:%f'%(p, r, f))
    return p, r, f