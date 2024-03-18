def checkFollowers():
    followed = open('saved/followed.txt', 'r', encoding='utf-8').read().splitlines()
    followers = open('saved/followers.txt', 'r', encoding='utf-8').read().splitlines()

    for i in followed:
        for j in followers:
            if i == j:
                break
        else:
            print(f'[i] That you follow, not follow you -> {i}')
            with open('saved/dedections.txt', 'a', encoding='utf-8') as file:
                file.write(i+'\n')