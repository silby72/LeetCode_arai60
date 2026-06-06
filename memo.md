
# step1まで
カウンターで数えるのはなくスタックで管理  

mapで対応関係を記す  

データ構造とアルゴリズムを使えないか考える

# step2まで
想定していない入力が来ることも考える

```python
return len(stack)  == 0
```

の方がいいかも

# step3まで
データ構造に名前ではなく構造名をつけるのは良くないとの指摘

## 他の方のコード
https://github.com/mamo3gr/arai60/blob/20_valid-parentheses/20_valid-parentheses/step3.py


````python
class Solution:
    def isValid(self, s: str) -> bool:
        OPEN_BRACKETS = ('(', '{', '[')
        open_to_close = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        stack = []
        for char in s:
            if char in OPEN_BRACKETS:
                stack.append(char)
                continue

            try:
                last_pushed = stack.pop()
            except IndexError:
                return False
            
            if open_to_close[last_pushed] == char:
                pass
            else:
                return False
        
        return len(stack) == 0
````

・)(ではなく()の方が直感的のため読みやすい  

・``for char in s:``のうほうがpythonだと主流らしいが、最近は組み込みのC++ばかりやっていたので``for i in range(len(s)):``と書いてしまう  

・エラーに対する考え方の違いはEAFPスタイルとLBYLスタイルというらしい

スタックが空のときにpopすると不味いのでダミーを入れる