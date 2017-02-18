
# encoding=utf-8
import jieba
import codecs

def segment(sentence,list,dicts):
    #jieba.suggest_freq("BOS",True)
    #jieba.suggest_freq("EOS",True)
    jieba.suggest_freq("今天",True)
    jieba.suggest_freq('天气',True)

    sentence = jieba.cut(sentence,HMM=False)
    format_sentence = ",".join(sentence)
    lists = format_sentence.split(",")

    length = len(lists)
    for i in range(length-1):
        word = lists[i]
        word_next = lists[i+1]
        if len(word) == 2 and len(word_next) == 2:
            word_new = word+" "+word_next
            #print(word_new)
            if word_new not in dicts:
                dicts[word_new] = 1
            else:
                dicts[word_new] +=1


def sort_by_value(d):
    items=d.items()
    backitems=[[v[1],v[0]] for v in items]
    backitems.sort()
    return [ backitems[i][1] for i in range(0,len(backitems))]


def delblankline(infile, outfile):
    """ Delete blanklines of infile """
    infp = codecs.open(infile, "r",encoding='utf-8')
    outfp = codecs.open(outfile, "w",encoding='utf-8')
    lines = infp.readlines()
    for li in lines:
        if li.split():
            outfp.writelines(li)
    infp.close()
    outfp.close()


if  __name__ == '__main__':

    #sentence_ori =u"经常有人问我如何开始学习机器学习，经常有人问我如何开始学习机器学习,他们面临的最大困难就是机器学习背后的数学原理。我承认其实我也不喜欢数学。数学是对事物的一种抽象描述，用数学来描述机器学习，会过于抽象，且不容易理解。因此在这个系列的文章中，我尝试使用伪代码或者JavaScript来描述我所讲述的内容"
    #sentence_ori =u"今天天气不错，非常适合出去游玩啊。"

    delblankline("happiness_seg.txt","data.txt")

    f = codecs.open("data.txt",'r',encoding='utf-8')
    sentence_ori = f.read()
    f.close()
    sentence_ori = sentence_ori.strip()
    sentence_ori = sentence_ori.replace(" ","")

    ori_list = []
    ori_dict = {}
    segment(sentence_ori,ori_list,ori_dict)

    # 注意返回的是list，而不是dict
    new_dict = sorted(ori_dict.items(), key=lambda x: x[1], reverse=True)

    for i in range(10):
        print(i,new_dict[i][0],new_dict[i][1])


## 简单教程参考 ： http://www.cnblogs.com/LgyBean/p/6263008.html
## https://segmentfault.com/a/1190000004959880
##　http://www.voidcn.com/blog/qq_24918869/article/p-6151570.html
