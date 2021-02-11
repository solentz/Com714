def q1():
    print("who broke my heart?")
    response = input()
    print(f"my first love {response} broke my heart for the first time")

q1()


def q2():
    print("who sees my rolling? (cops,wardens,other)")
    response = input()
    print(f"they see my rolling.they hating.they hoping they gonna catch me riding dirty! {response} my music's so loud.i'm swanging.they hoping they gonna catch me riding dirty!")

q2()


def q3():
    num_list = []
    break_free = input("how many times should i break free:")
    break_free = int(break_free)
    print("i'm stronger than i have been before...")
    print(break_free)
    for i in range(break_free):
        num_list.append(i)

    num_list.reverse()
    for j in num_list:
        print(f"{j}: this is the part when i break free....")
        if j == 1:
            break

    print("cause i can't resist it no more")


q3()

