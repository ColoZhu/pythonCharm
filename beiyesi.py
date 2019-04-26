def bayesFunc(pIsBox1, pBox1, pBox2):
    return (pIsBox1 * pBox1) / ((pIsBox1 * pBox1) + (1 - pIsBox1) * pBox2)


def redGreenBallProblem():
    # 甲事件的先验概率
    pIsBox1 = 0.5
    # consider 8 red ball
    for i in range(1, 9):
        pIsBox1 = bayesFunc(pIsBox1, 0.7, 0.3)
        print(" After red %d > in 甲 box: %f" % (i, pIsBox1))

    # consider 4 green ball
    for i in range(1, 5):
        pIsBox1 = bayesFunc(pIsBox1, 0.3, 0.7)
        print(" After green %d > in 甲 box: %f" % (i, pIsBox1))

redGreenBallProblem()
