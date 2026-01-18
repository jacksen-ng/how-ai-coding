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
