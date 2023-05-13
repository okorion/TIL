## 🌲 Tree data structure in JavaScript

<br>

## ![post-thumbnail](https://velog.velcdn.com/images/chltmdxo3/post/290db01a-c6ed-461a-a0a6-4c5eff1f6613/image.png)

<br>

트리는 굉장히 흥미로운 데이터 구조입니다. 모든 분야들에서 다양한 응용성을 가집니다.
예를들어:

- DOM은 하나의 트리 데이터 구조다.
- 우리 운영체제에서 Directory와 files들은 트리구조로 표현될 수 있다.
- 가족계층(A family hierarchy)은 트리구조로 표현될 수 있다.

트리 구조로부터 파생된 모든 구조들(힙, BST 등)은 스케줄링, 이미지 프로세싱, DB등의 구조에서 사용될 수 있습니다. 많은 복잡한 데이터 구조들은 한 눈에 보기에는 트리구조와 관련 없어 보이지만 실제로는 하나로 표현될 수 있습니다. 우리는 시리즈로 제공될 문제들을 통해 트리구조가 어떻게 복잡해 보이는 문제들을 쉽게 파악하고 푸는지 볼 것입니다.

<br>

서론
이진 트리 구조로 Node를 구현하는 것은 간단합니다.

```null
function Node(value){
  this.value = value
  this.left = null
  this.right = null
}
// usage
const root = new Node(2)
root.left = new Node(1)
root.right = new Node(3)
```

<br>

이 몇 줄 안되는 코드는 아래와같은 이진 트리구조를 생성합니다.

```null
           2  
        /      \
       /         \
     1            3
   /   \        /    \
null  null   null   null
```

참 쉽죠잉?! 그럼 어떻게 사용해야할까요?

<br>

순회
이 연결된 트리 노드들로 시작해봅시다. 하나의 배열을 반복하는 것처럼 트리 노드들을 반복한다면 좋을것 같습니다. 그런데 트리구조는 배열처럼 한 줄로 나열된 데이터 구조가 아니기 때문에 순회에는 하나의 방향만 있을 수는 없습니다. 대략적으로 순회 접근은 다음과 같이 분류할 수 있습니다.

- 넓이 우선 탐색 (BFS)
- 깊이 우선 탐색 (DFS)

<br>

넓이 우선 탐색 (BFS)
BFS는 트리를 레벨별로 탐색합니다. 루트 노드에서 시작해서 해당 노드의 모든 자식을 거치고 두번째 레벨의 자식들을 거치는 작업을 계속합니다. 예를들어 위에서 그렸던 트리구조의 순회결과는 이러합니다.

```null
2, 1, 3
```

<br>

약간의 복잡한 트리구조의 이해를 돕기위해 그림을 넣어봤습니다.
![img](https://velog.velcdn.com/images%2Fchltmdxo3%2Fpost%2F8459a99a-97ed-4eab-a970-10148fde5edf%2FMEa_jdswt.jpeg)

<br>

이 형태의 데이터 구조를 가진 순회를 하기 위해서 큐(queue)를 이용할 수 있습니다. 전체 알고리즘은 다음과 같습니다.

1. 루트로 큐를 초기화 시킨다.
2. 큐에서 첫번째 아이템을 제거(shift)한다.
3. 뽑은 아이템의 좌, 우 자식을 큐에 넣는다(push).
4. 큐가 비워질 때까지 반복한다.

<br>

아래는 알고리즘 구현 후의 모습이다.

```null
function walkBFS(root){
  if(root === null) return

  const queue = [root]
  while(queue.length){
      const item = queue.shift()
      // do something
      console.log(item)

      if(item.left) queue.push(item.left)
      if(item.right) queue.push(item.right)
   }
}
```

<br>

위의 알고리즘을 조금만 수정하면 레벨별로 표현된 이중 배열형태로 값을 반환 받을 수 있습니다.

```null
function walkBFS(root){
  if(root === null) return

  const queue = [root], ans = []

  while(queue.length){
      const len = queue.length, level = []
      for(let i = 0; i < len; i++){
          const item = queue.shift()
          level.push(item)
          if(item.left) queue.push(item.left)
          if(item.right) queue.push(item.right)
       }
       ans.push(level)
   }
  return ans
}
```

<br>

깊이 우선 탐색 (DFS)
DFS는 노드하나를 선택한 뒤 계속해서 더 이상 자식노드가 없을 때까지 자식노드를 탐색합니다.
다음 세가지 방법중 하나로 수행할 수 있습니다.

```null
 root node -> left node -> right node // pre-order traversal
 left node -> root node -> right node // in-order traversal
 left node -> right node -> root node // post-order traversal
```

이 모든 순회기법들은 재귀적으로 또 반복적으로 수행 할 수 있습니다.
수행하는 과정을 자세히 들여다 봅시다.

<br>

전위순회(preorder traversal)

트리형태의 전위순회는 다음과 같은 형태를 보입니다.

```null
 root node -> left node -> right node
```

![img](https://cdn.hashnode.com/res/hashnode/image/upload/v1630066335323/uu_rnMwc2.png?auto=compress,format&format=webp)

<br>

방법
이 간단한 기법으로 어떠한 트리에서도 전위순회를 수행할 수 있습니다.
트리의 루트노드에서 시작해서 계속해서 왼쪽에 있는 노드를 순회합니다.

![img](https://cdn.hashnode.com/res/hashnode/image/upload/v1630066309451/tKaff2RAo0.png?auto=compress,format&format=webp)

<br>

구현
실제 순회 구현을 해봅시다. 재귀적인 접근은 굉장히 직관적입니다.(알기 쉽다?)

```null
function walkPreOrder(root){
  if(root === null) return

  // do something here
  console.log(root.val)

  // recurse through child nodes
  if(root.left) walkPreOrder(root.left)
  if(root.right) walkPreOrder(root.right)
}
```

<br>

스택대신 큐를 사용하고 스택에 우측 자식을 먼저 대입하는것을 제외하곤 전위순회를 위한 반복적이 접근은 BFS와 상당히 유사합니다.

```null
function walkPreOrder(root){
  if(root === null) return

  const stack = [root]
  while(stack.length){
      const item = stack.pop()

      // do something
      console.log(item)

      // Left child is pushed after right one, since we want to print left child first hence it must be above right child in the stack
      if(item.right) stack.push(item.right)
      if(item.left) stack.push(item.left)
   }
}
```

<br>

중위순회
중위순회의 트리는 다음과 같습니다.

```null
root node -> left node -> right node
```

![img](https://cdn.hashnode.com/res/hashnode/image/upload/v1630066398214/_S82oVUdj.png?auto=compress,format&format=webp)

<br>

방법
이 간단한 기법으로 어떠한 트리에서도 중위순회를 수행할 수 있습니다.
수평상태의 평면거울을 트리의 아래에 두고 모든 노드들을 비춰봅시다.

<br>

구현
재귀적으로 구현하기

```null
function walkInOrder(root){
  if(root === null) return

  if(root.left) walkInOrder(root.left)

 // do something here
  console.log(root.val)

  if(root.right) walkInOrder(root.right)
}
```

<br>

반복적으로 구현하기
해당 알고리즘을 처음엔 약간 이해하기 어려울 수 있습니다. 그런데 이건 꽤나 직관적입니다.
이렇게 봐봅시다. 중위순회에선 대부분 좌측 자식이 먼저 출력된 후 루트 그리고 우측이 출력됩니다.
그래서 처음은 이렇게 생각하면 좋습니다.

```null
const curr = root

while(curr){
  while(curr.left){
    curr = curr.left // get to leftmost child
  }

  console.log(curr) // print it

  curr = curr.right // now move to right child
}
```

<br>

위와같은 접근방식은 역추적이 어렵습니다. 즉 부모 노드로 돌아가는 것은 대부분 좌측 노드로 돌아가는 것입니다. 그래서 기록하기위한 스택이 필요합니다. 그래서 접근방식을 수정하면 다음과 같습니다.

```null
const stack = []
const curr = root

while(stack.length || curr){
  while(curr){
    stack.push(curr) // keep recording the trail, to backtrack
    curr = curr.left // get to leftmost child
  }
  const leftMost = stack.pop()
  console.log(leftMost) // print it

  curr = leftMost.right // now move to right child
}
```

<br>

이제 위 접근방식을 사용하여 최종반복 알고리즘을 작성할 수 있습니다.

```null
function walkInOrder(root){
  if(root === null) return

  const stack = []
  let current = root

  while(stack.length || current){
      while(current){
         stack.push(current)
         current = current.left
      }
      const last = stack.pop()

      // do something
      console.log(last)

      current = last.right
   }
}
```

<br>

후위순회
후위순회는 다음과같은 트리 구조를 가집니다.

```null
Left node -> right node -> root node
```

![img](https://cdn.hashnode.com/res/hashnode/image/upload/v1630066468275/aXvp4kZ-V.png?auto=compress,format&format=webp)

방법
모든 트리의 빠른 후위순회는 좌측의 노드들을 하나씩 뽑아내는 것이다.

![img](https://cdn.hashnode.com/res/hashnode/image/upload/v1630066456516/oWu_cm681.png?auto=compress,format&format=webp)

구현
재귀적으로 구현하기

```null
function walkPostOrder(root){
  if(root === null) return

  if(root.left) walkPostOrder(root.left)
  if(root.right) walkPostOrder(root.right)

  // do something here
  console.log(root.val)

}
```

<br>

반복적으로 구현하기
이미 전위순회에서 반복적으로 구현한적 있습니다. 재활용 해 볼까요?
후위순회는 전위순회를 그냥 뒤집은 것처럼 보입니다.

```null

// PreOrder:
root -> left -> right

// Reverse of PreOrder:
right -> left -> root

// But PostOrder is:
left -> right -> root
```

<br>

아주 조금 다릅니다. 하지만 전위순회를 조금 수정하고 뒤집음으로써 후위순회의 결과를 얻을 수 있습니다.

다음과 같습니다.

```null
// record result using
root -> right -> left

// reverse result
left -> right -> root
```

전위순회에서 반복적인 방식을 사용한것처럼 부분적으로 스택을 사용합니다.
다른점은 root -> right -> left 순서대신 root -> left -> right라는 점입니다.
결과 배열에 계속 순회의 연속을 기록합니다.
결과를 뒤집으면 후외순회가 나타납니다.

```null
function walkPostOrder(root){
  if(root === null) return []

  const tempStack = [root], result = []

  while(tempStack.length){
      const last = tempStack.pop()

      result.push(last)

      if(last.left) tempStack.push(last.left)
      if(last.right) tempStack.push(last.right)
    }

    return result.reverse()
}
```

+자바스크립트 팁

이렇게만 트리를 순회할 수 있다면 얼마나 좋을까요?

```null
for(let node of walkPreOrder(tree) ){
   console.log(node)
 }
```

보기에 진짜 좋아보이고 읽기 쉬워보입니다. walk함수를 사용하기만 하면 됩니다.

<br>

다음은 walkPreOrder함수를 위와 같이 동작하도록 수정한 것입니다.

```null
function* walkPreOrder(root){
   if(root === null) return

  const stack = [root]
  while(stack.length){
      const item = stack.pop()
      yield item
      if(item.right) stack.push(item.right)
      if(item.left) stack.push(item.left)
   }
}
```

<br>

원문:[Tree data structure in JavaScript (stackfull.dev)](https://stackfull.dev/tree-data-structure-in-javascript)

<br>

<br>

#### 참고링크: [자바스크립트에서의 트리 데이터 구조 [번역\] (velog.io)](https://velog.io/@chltmdxo3/자바스크립트에서의-트리-데이터-구조-번역중)

<br>