import term_io
from guess_numbers import guess_a_number
from account_manage import account
import connect_five

def run_connect_five():
    print("It's a game to get five pieces connected into a line first, either horizontally, vertically or diagonally.")
    print("Your pieces are 'O'. Type coordinate with row + colume. For example H row and K col, key in hk.")
    print("Choose a difficulty level. The higher level you chose, the longer time computer would use.")
    reward=[150,250,450]
    action = term_io.select_menu([
                            "  Easy  ",
                            "  Hard  ",
                            "  Guru  ",
                            "  Exit  "])
    if action==3:
        return 0
    else:
        if connect_five.gamemain(action+1)==0:
            print("No reward for losing a game.")
            term_io.press_any_key_to_continue()
            return 0
        else:
            return reward[action]
            
        
def minigame(user):
    while True:
        print(term_io.fgcolor.black+term_io.bgcolor.yellow+ "  Mini Game Room  "+term_io.fgcolor.reset)
        print("Winning a minigame will earn you points. But sometimes, losing it will also takes a few points from you.\n")
        action = term_io.select_menu([
        "  Guess a Number  ",
        "   Connect Five   ",
        "   Exit the Room  "])
        points_gain=0
        if action==2:
            return user
        elif action==0:
            print(
                "\n\n\nYou will gain 50 points if winning the game, but lose 5 points if failed.")
            if guess_a_number():
                print(term_io.fgcolor.green+"You gained 50 points."+term_io.fgcolor.reset)
                user.points += 50
            else:
                print(term_io.fgcolor.red+"You lost 5 points."+term_io.fgcolor.reset)
                user.points -= 5
                if user.points<0:
                    user.points=0
            user.save()
            term_io.press_any_key_to_continue()
        elif action==1:
            points_gain=run_connect_five()
            if points_gain>0:
                print(term_io.fgcolor.green+"You got %d points!"%points_gain+term_io.fgcolor.reset)
                user.points+=points_gain
                user.save()
                term_io.press_any_key_to_continue()
            
                
def main():
    #print_team()
    user = account("test", "test")
    user.emoji_you_have = [3] * 7
    user=minigame(user)
    print("you got %d points."%user.points)

if __name__ == "__main__":
    main()