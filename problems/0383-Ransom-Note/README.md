## 383. 赎金信
https://leetcode-cn.com/problems/ransom-note/

## 题目描述
```
为了不在赎金信中暴露字迹，从杂志上搜索各个需要的字母，组成单词来表达意思。

给你一个赎金信 (ransomNote) 字符串和一个杂志(magazine)字符串，判断 ransomNote 能不能由 magazines 里面的字符构成。

如果可以构成，返回 true ；否则返回 false 。

magazine 中的每个字符只能在 ransomNote 中使用一次。

 

示例 1：

输入：ransomNote = "a", magazine = "b"
输出：false
示例 2：

输入：ransomNote = "aa", magazine = "ab"
输出：false
示例 3：

输入：ransomNote = "aa", magazine = "aab"
输出：true
```

## 思路
创建一个26长度的列表用来储存所有英文字母的小写，用列表的索引来表示是哪个字母  

`0` = `a`  
`1` = `b`   
`25` = `z`

获取`magazine`所有的字母一个个往列表中根据字母对应的索引上面自增  
同理，获取`ransomNote`所有的字母一个个往列表上面自减，并判定当前的字母是否小于`0`  
如果小于`0`的话，`magazine`就拼接不出`ransomNote`，如果都不小于`0`的话就成功

## 代码
Python
```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 如果ransomNote长度大于magazine的长度的话，magazine一定拼接不出ransomNote
        if len(ransomNote) > len(magazine):
            return False

        alphabet = [0] * 26

        for c in magazine:
            alphabet[ord(c) - ord("a")] += 1

        for c in ransomNote:
            alphabet[ord(c) - ord("a")] -= 1

            if alphabet[ord(c) - ord("a")] < 0:
                return False

        return True
```
