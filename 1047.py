tempos = list(map(int,input().split()))
hInic = tempos[0]
mInic = tempos[1]
hFin = tempos[2]
mFin = tempos[3]

if hFin > hInic and mFin >= mInic:
    hTot = hFin - hInic
    mTot = mFin - mInic
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hTot,mTot))
elif hFin > hInic and mFin < mInic:
    hTot = hFin - hInic - 1
    mTot = mFin - mInic + 60
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hTot,mTot))
elif hFin < hInic and mFin >= mInic:
    hTot = hFin - hInic + 24
    mTot = mFin - mInic
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hTot,mTot))
elif hFin < hInic and mFin < mInic:
    hTot = hFin - hInic + 23
    mTot = mFin - mInic + 60
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hTot,mTot))
elif hFin == hInic and mFin > mInic:
    hTot = hFin - hInic
    mTot = mFin - mInic
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hTot,mTot))
elif hFin == hInic and mFin == mInic:
    hTot = 24
    mTot = mFin - mInic
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hTot,mTot))