# -*- coding: UTF-8 -*-
from pypinyin import pinyin, lazy_pinyin,Style
import re
import codecs
class getShapeFeature:
    def __init__(self):
        #笔画数
        self.strokes = []
        strokes_path='zh_dict/strokes.txt'
        with open(strokes_path, 'r') as fr:
            for line in fr:
                stroke=line.strip()
                if int(stroke)<10:
                    self.strokes.append(stroke)
                elif int(stroke)>35:
                    self.strokes.append('Z')
                else:
                    self.strokes.append(chr(int(stroke)+55))
        #结构
        ids_path='zh_dict/ids.txt'
        self.ids={}
        idsFix={'⿰':'1','⿱':'2','⿲':'3','⿳':'4','⿴':'5','⿵':'6','⿶':'7','⿷':'8','⿸':'9','⿹':'A','⿺':'B','⿻':'C'}
        with open(ids_path, 'r') as fr:
            for line in fr:
                items=line.split('\t')
                if len(items)>1:
                    if items[1]==items[2].strip('\n') :
                        self.ids[items[1].decode('utf-8')]='0';
                    else:
                        if idsFix.has_key(line[11:14]):
                            self.ids[items[1].decode('utf-8')]=idsFix[line[11:14]]
        #四角号码
        self.MB = {}
        MB_path='zh_dict/MB.txt'
        f=codecs.open(MB_path,'r','utf-8-sig')
        for line in f:
            self.MB[line[0:1]]=line[1:5]

    def getStroke(self,word):
        unicode_ = ord(word)
        if 13312 <= unicode_ <= 64045:
            return self.strokes[unicode_-13312]
        elif 131072 <= unicode_ <= 194998:
            return self.strokes[unicode_-80338]
        else:
            return '-1'
        
    def getShapeFeature(self,word):
        self.word=word.decode('utf-8')
        shapeFeature=[]
        for i in self.word:
            tmp=[]
            tmp.append(self.ids[i])
            for s in self.MB[i]:
                tmp.append(s)
            tmp.append(self.getStroke(i))
            shapeFeature.append(tmp)
        return shapeFeature
