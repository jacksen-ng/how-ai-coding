# 例の使い方

## 1. 与えたプロンプト

```bash
Pythonで簡単なゲームを作りたいですけど、どうすればいいのか？AGENTSmdのルールを従ってください。Exampleの下に作成してください
```

## 2. 出してくれた提案

```bash
AGENTS.mdのルールを確認しました。ルール3に従って、まずコードを直接変更せず、2つの解決策を提案します。

Pythonで簡単なゲームを作成 - 提案
解決策1: 数当てゲーム（Number Guessing Game）
概要: コンピュータがランダムな数字を選び、プレイヤーがその数字を当てるゲーム

選択理由:

Pythonの基礎（変数、条件分岐、ループ）を学ぶのに最適
外部ライブラリ不要（標準ライブラリのみ使用）
Pros:

シンプルで初心者向け
すぐに実装可能
コンソールだけで動作
Cons:

ビジュアル要素がない
ゲーム性がシンプル
影響モジュール: なし（新規作成）

変更予定ファイル:

ファイルパス	変更タイプ
example/number_guessing_game.py	新規作成
解決策2: じゃんけんゲーム（Rock Paper Scissors）
概要: プレイヤーとコンピュータがじゃんけんで対戦するゲーム

選択理由:

馴染みのあるゲームで理解しやすい
基礎的なPython構文を網羅
Pros:

ルールが分かりやすい
拡張しやすい（スコア機能など）
標準ライブラリのみで実装可能
Cons:

ビジュアル要素がない
ランダム性に依存
影響モジュール: なし（新規作成）

変更予定ファイル:

ファイルパス	変更タイプ
example/rock_paper_scissors.py	新規作成
どちらを実装しますか？
数当てゲーム - 数字を当てるシンプルなゲーム
じゃんけんゲーム - コンピュータとじゃんけん対戦
どちらかを選んでください！（または別のゲームのリクエストがあればお知らせください）
```

## 3. 与えた選択

```bash
じゃんけんゲーム
```

## 4. 実装したコード

```python
import random


def get_computer_choice():
    choices = ["グー", "チョキ", "パー"]
    return random.choice(choices)


def get_player_choice():
    print("\n手を選んでください:")
    print("1: グー")
    print("2: チョキ")
    print("3: パー")
    print("0: ゲーム終了")

    while True:
        try:
            choice = int(input("番号を入力: "))
            if choice == 0:
                return None
            elif choice == 1:
                return "グー"
            elif choice == 2:
                return "チョキ"
            elif choice == 3:
                return "パー"
            else:
                print("1、2、3のいずれかを入力してください")
        except ValueError:
            print("有効な番号を入力してください")


def determine_winner(player, computer):
    if player == computer:
        return "draw"

    winning_combinations = {
        "グー": "チョキ",
        "チョキ": "パー",
        "パー": "グー"
    }

    if winning_combinations[player] == computer:
        return "player"
    return "computer"


def display_result(player, computer, result):
    print(f"\nあなた: {player}")
    print(f"コンピュータ: {computer}")

    if result == "draw":
        print("結果: あいこ!")
    elif result == "player":
        print("結果: あなたの勝ち! 🎉")
    else:
        print("結果: コンピュータの勝ち! 😢")


def main():
    print("=" * 40)
    print("     じゃんけんゲーム")
    print("=" * 40)

    player_wins = 0
    computer_wins = 0
    draws = 0

    while True:
        player_choice = get_player_choice()

        if player_choice is None:
            break

        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)
        display_result(player_choice, computer_choice, result)

        if result == "player":
            player_wins += 1
        elif result == "computer":
            computer_wins += 1
        else:
            draws += 1

        print(f"\n[スコア] あなた: {player_wins} | コンピュータ: {computer_wins} | あいこ: {draws}")

    print("\n" + "=" * 40)
    print("     最終結果")
    print("=" * 40)
    print(f"あなたの勝ち: {player_wins}")
    print(f"コンピュータの勝ち: {computer_wins}")
    print(f"あいこ: {draws}")
    print("ゲームを終了します。ありがとうございました!")


if __name__ == "__main__":
    main()
```
