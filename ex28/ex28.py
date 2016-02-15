def Tester(statement, expected):
    """Tests whether the statement and the expected answer are the same."""
    if statement == expected:
        print "Correct."
    else:
        print "Incorrect. %r does not equal %r." % (statement, expected)


Tester(True and True, True)
Tester(False and True, False)
Tester(1 == 1 and 2 == 1, False)
Tester("test" == "test", True)
Tester(1 == 1 or 2 != 1, True)
Tester(True and 1 == 1, True)
Tester(False and 0 != 0, False)
Tester(True or 1 == 1, True)
Tester("test" == "testing", False)
Tester(1 != 0 and 2 == 1, False)
Tester("test" != "testing", True)
Tester("test" == 1, False)
Tester(not (True and False), True)
Tester(not (1 == 1 and 0 != 1), False)
Tester(not (10 == 1 or 1000 == 1000), False)
Tester(not (1 != 10 or 3 == 4), False)
Tester(not ("testing" == "testing" and "Zed" == "Cool Guy"), True)
Tester(1 == 1 and (not ("testing" == 1 or 1 == 0)), True)
Tester("chunky" == "bacon" and (not (3 == 4 or 3 == 3)), False)
Tester(3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")), False)
