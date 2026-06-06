
# step1まで
スタックとポインタを使って管理

スタックから取り出した値をノードとして繋ぎ直す処理が必要  
これにはdummy使う  
``.pop()``で取り出されるのはintのみ

新しくnodeを生成してつなぎ直してるため効率が悪いと感じた　　

# step2まで

（別解）再帰で解く方法もあるらしい

````python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def _reverse_linked_list(head, previous):
            if head is None:
                return previous
            temp = head.next
            head.next = previous
            return _reverse_linked_list(temp, head)
        return _reverse_linked_list(head, None)
````
・


（別解）ポインタ反復で解く方法もあるらしい

````python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr is not None:
            next_node = curr.next
            
            curr.next = prev
            
            prev = curr
            curr = next_node

        return prev
````

・英弱なので変数名を``new_node``などに変更する

# step3まで

## 他の方のコード

https://github.com/olsen-blue/Arai60/blob/olsen-blue-patch-7/206.%20Reverse%20Linked%20List.md