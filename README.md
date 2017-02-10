
# JTPA DL hands-on course materials
for Feb/2017 JTPA Deep Learning meetup

## overview 
We will try **"Learn TensorFlow and deep learning, without a Ph.D"**

[https://cloud.google.com/blog/big-data/2017/01/learn-tensorflow-and-deep-learning-without-a-phd](https://cloud.google.com/blog/big-data/2017/01/learn-tensorflow-and-deep-learning-without-a-phd)


+ Chapter 1: 手書き文字認識のtensorflowチュートリアル

```
mnistと呼ばれる 28x28サイズの手書きの数字データセットに対して、0から9までの数字に分類するタスクです。

tensorflowの最初のチュートリアルとして有名。このチュートリアルを読みながら実際に手書き文字を認識するモデルを構築します。
```

+ Chapter 2: tensorflowの基礎知識やDLの基本手法

```
tensorflowを使って簡単な二元一次方程式を解いたりANDやXORのロジックを学習させるのを試します。

あるいはmnistの最初のチュートリアルを終えた方向けに、mnistのより複雑なモデルを実装しウェイトの初期化方法の違いやdrop outの実装を試します。
```


+ Chapter 7: RNNによるテキスト処理のtensorflowチュートリアル

```
RNN(LSTM)を使った文章内の次の単語を予測するチュートリアルを実装します。

画像よりもテキストやRNNに興味がある方向けです。
```

+ Chapter 8: Google Cloud Machine Learning Platformの試用

```
GoogleのCloud Machine Learning Platform を試用し、手持ちの画像の認識やテキストの解析を試します。

tensorflowやディープラーニングの技術そのものよりも最新の機械学習モデルの性能に興味がある方向けです。
```


# environment

Please install tensorflow and python. 

+ [tensorflow.org](https://www.tensorflow.org)

+ [python.org](https://www.python.org)

Recommended IDE is PyCharm.

+ [PyCharm](https://www.jetbrains.com/pycharm/)


# Chapter 1: 手書き文字認識

[Slides](https://docs.google.com/presentation/d/1TVixw6ItiZ8igjp6U17tcgoFrLSaHWQmMOwjlgQY9co/pub?slide=id.p)

[Video](https://www.youtube.com/watch?v=qyvlt7kiQoI&feature=youtu.be)

[tutorial](https://www.tensorflow.org/tutorials/mnist/beginners/)

# Chapter 2: tensorflowの基礎知識、DLの基本手法

[Slides](https://docs.google.com/presentation/d/1TVixw6ItiZ8igjp6U17tcgoFrLSaHWQmMOwjlgQY9co/pub?slide=id.g110257a6da_0_13)

[Video](https://www.youtube.com/watch?v=qyvlt7kiQoI&t=1m12s)

[tutorial](https://www.tensorflow.org/tutorials/mnist/pros/)

あるいはより基礎的なお題として下記の問題を解いてみて下さい。

```
[演習 1]

りんごを3個、バナナを1個買ったら560円、

りんごを2個、バナナを2個買ったら640円でした。それぞれ幾らでしょうか？

[演習 2]

AND、OR、XORのロジックを学習により得るモデルを作ってみて下さい。
```

# Chapter 7: RNNによるテキスト処理

[Slides](https://docs.google.com/presentation/d/e/2PACX-1vRouwj_3cYsmLrNNI3Uq5gv5-hYp_QFdeoan2GlxKgIZRSejozruAbVV0IMXBoPsINB7Jw92vJo2EAM/pub#slide=id.g17d56f1df3_0_106)

[Video](https://www.youtube.com/watch?v=vq2nnJ4g6N0&t=107m25s)

[tutorial](https://www.tensorflow.org/tutorials/recurrent/)


# Chapter 8: Google Cloud Machine Learning Platform
[Slides](https://docs.google.com/presentation/d/e/2PACX-1vRouwj_3cYsmLrNNI3Uq5gv5-hYp_QFdeoan2GlxKgIZRSejozruAbVV0IMXBoPsINB7Jw92vJo2EAM/pub?slide=id.g963e5b4287fb24d_677)

[Video](https://www.youtube.com/watch?v=zqWt8oI4gEw&feature=youtu.be&t=23m6s)

[CLOUD MACHINE LEARNING PLATFORM](https://cloud.google.com/products/machine-learning/)
