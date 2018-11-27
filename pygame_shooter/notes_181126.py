# loops in general; organizing github to find what I need and the overall
# process of submitting a new

# For vs. while
#     for - specific # of iterations
#     while - go until condition is met
# while - should have a condition that is clear about when to stop
#     continue and break should never be necessary in a while loop
#     they make it hard to read your code

# students = [1, 2, 34, 5, 6, 78, 3, 4]
# for i in range(1, len(students)):


# game_on, keep_playing, is_alive
# while(game_on< 50)
user_input = 5
for i in range(1,11):
    for j in range(1,11):
        if j == user_input:
            # stop the loop
            # break;
            # stop this iteration
            continue;

        print i, j
    print "Inside loop is done"
print "Both loops are done"