import random
print("数当てゲームを始めます")
print("答えの数の範囲は1~100です")

answer = random.randrange(start=1, stop=100)
guess = int(input("あなたが予想する数字:"))
print(guess)
print(type(guess))
tries = 1

while guess !=answer: # !=(ノットイコール)比較演算子:snake2で確認
    # 予想が外れている限り、whileの中身を実行する
    if guess > answer:
        print("あなたの予想した数は答えより大きいです")
    else:
        print("あなたの予想した数は答えより小さいです")

    tries = tries + 1
    guess = int(input("あなたが予想する数字:"))

# whileが終了したので予想が当たった。
print("正解です。答えは{}".format(answer))
print("あなたの試行回数は{}でした".format(tries))

# # ここに戻りたい
# if guess == answer:
#     print("正解です。答えは{}".format(answer))
#     print("あなたの試行回数は{}でした".format(tries))

# else:
#     if guess > answer:
#         print("あなたの予想した数は答えより大きいです")
#     else:
#         print("あなたの予想した数は答えより小さいです")

# tries = tries + 1
# guess = int(input("あなたが予想する数字:"))
# # もう一度繰り返したい

"""
他に昨日追加をするなら
・guessが1~100以外だったエラー表示
・guessが文字列だったらエラー表示
・guessが小数だったら小数切り捨てしたことがわかるように表示
・試行回数がN回以上になったら自動的にゲーム終了
・予想が当たる確率を表示してゲームを盛り上げる
"""

"""
今回のポイント
if文ではなくてwhile文を使うところ。
while文を使うといろいろターミナルで遊べるゲームを作ることができる。
"""
