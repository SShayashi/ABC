
### 098 validate binary search
- 初見で解けた: true

最初は定義を読み間違えていた．

最初は，BSTにおいて，「親の左の子は親より小さい」と読んだ．実際には「親の左のサブツリーのノードは親より小さい」だった．

最大値と最小値をもたせながら深さ優先を行うことで処理できた．

### 121 Best Time to Buy and Sell Stock
- 初見で解けた: false

初見では愚直な方法しか思いつかず Time exceeded
o(n)の解法はmin valueを更新しつつ，最大利益を更新し続ける
自分は `i-1 > i < i+1` のときminを更新， `i-1 < i > i+1` のときmaxを更新して
最終利益を `max -min` で計算したが，これでは [2,1,2,0,1] みたいな後半に再度minが更新される場合，minは0，maxが2になって
エラーになる．

### 347

- 初見で解けた: True?

制限が`O(n log n)`とあったので，hashとsortを使って解いた．

一方で，想定解法は`O(nlog k )`だった．最悪の場合k=nなので，`O(nlogn)`自分のコードでもpassした．

想定解法では，heapを使う．取得した要素とその出現回数を利用して，出現回数のmax-heapを構築．top-kを返す．
heapはn=1はminと変わらない，またn>=heap.sizeのときはsortと変わらない．それ以外の場合において高速っぽい．
heapは，データの挿入は`O(log n)`で可能．最大値（最小値）の取得も`O(log n)`，今回の問題の場合，出現回数で`priority queue`を実装して，top k 件を取得する．
keyのユニークな数はk個，最大n回keyを足すので`n log k`.


### 387 First Unique Character in a String
- 初見で解けた: True

愚直にHashを使った．
解法を見ると，pythonのcollectionsのcountを使うとよりコードが短くなることがわかった．


### 392 Is Subsequence
- 初見で解けた: true

追加問題にて，入力sが複数ある場合の処理方法はどうすべきか？という問題があった．
discussionを見る限りだと，入力tから，各文字をkeyとするhashを作る．
keyの要素は，その文字が現れたindexを表す．
例えば，`abcdefab`の場合以下のhashが作られる．
```json
{
  "a": [1,7],
  "b": [2,8],
  "c": [3],
  "d": [4],
  "e": [5],
  "f": [6]
}
```

次に入力s1を見る場合は，s[0]をkeyにもつhashの要素を見つけ，最初は最も少ない数字を見つける．
その最も少ない数字を`prev` 変数として持っておき，次のkeyを探す時に利用する．次に探すときは
`prev` 以上で，最も少ない数字を探す．このとき二分探索が利用できる．もし，二分探索で見つけられない場合，
回答は`false`となる．

### 394  Intersection of Two Arrays

初見: true

最悪のケースだと`O(M*N)`になる．
最悪のケースは，MにもNにも共通の要素がないとき

>This is a Facebook interview question.
They ask for the intersection, which has a trivial solution using a hash or a set.
>
>Then they ask you to solve it under these constraints:
>O(n) time and O(1) space (the resulting array of intersections is not taken into consideration).
You are told the lists are sorted.

Facebookで出された問題

条件：
- 時間計算量 `O(n)`，空間計算量`O(1)`（答え用の配列は空間計算量に含まない）
- 与えられるリストがソートされている

双方の配列を0から順に見て，どちらかが超えていれば，少ない方の要素番号をインクリメント
同じ値のときのみans配列に入れる．

### 560 subarray sum equals k
- 初見で解けた: false

初見では累積和を使って処理した．o(n^2)ではtime exceeded だった．

`o(n)`の解法理解した
`（累積和 - k）`をkeyにしてhash作成する．`（累積和 - k）`が見つかったとき，ans+=1 する．
`（累積和 - k）`の意味を考える．
累積和の合計からkを引いて現れるkeyの出現が2回目のとき，
合計がkになる組み合わせが1つ存在していることを表す．

### 617 merge two binary tree
- 初見で解けた: false

特にコメントはない

### 929 unique email addresses
- 初見で解けた: true

想定解法を見ると，`+`を見つけるのに `index`関数を使っていた．
自分は`for`文で行っていたので，orderを確認した．
確認したところ，`index`関数も愚直に開始位置から順に見ていたので，速度的にはあまり変わりなさそうだった．