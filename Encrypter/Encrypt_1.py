import time
import os
import _console

try:
    def encrypter(Coder):
        _console.clrscr()
        #staring logo and here the screen has to be cleared
        print('''\n\n                                    uuuuuuu
                                    uu   uu
                                    uu   uu
                                    uu   uu
                                  uuuuuuuuuuu
                                  uuuuuuuuuuu
                                  uuuuuuuuuuu
                                  uuuuuuuuuuu

    EEEEEEEEE  NNN    NN  CCCCCCCCC  RRRRRRR   YY     YY  PPPPPP   TTTTTTTTTT
    EE         NNNN   NN  CC         RR    RR   YY   YY   PP   PP      TT
    EE         NN NN  NN  CC         RR    RR    YY YY    PP   PP      TT
    EEEEEEEEE  NN  NN NN  CC         RRRRRRRR     YYY     PPPPPP       TT
    EE         NN   NNNN  CC         RR   RR       Y      PP           TT
    EE         NN    NNN  CC         RR    RR      Y      PP           TT
    EEEEEEEEE  NN     NN  CCCCCCCCC  RR    RR      Y      PP           TT''')


        print("\n\n                     ###CREATED BY MANOJ PARAMSETTI###\n\n\n")
        Output=''
        #matching with already calculated encryption
        A='4897'
        B='5495'
        C='4849'
        D='8440'
        E='8599'
        D='9358'
        F='8044'
        G='4489'
        H='8989'
        I='4789'
        J='4940'
        K='4491'
        l='9440'
        m='8780'
        n='4084'
        o='4047'
        p='7944'
        q='7950'
        r='9644'
        s='9544'
        t='4955'
        u='4454'
        v='4944'
        w='8944'
        x='6494'
        y='8494'
        z='4949'

        space='7070'

        one='8879'
        two='7444'
        three='8994'
        four='4944'
        five='4444'
        six='8948'
        seven='9974'
        eight='5555'
        nine='2377'
        zero='5049'

        dot='4944'
        comma='4499'
        exclam='4444'
        quote='9098'
        Dquote='4444'
        colon='4949'
        semicolon='4944'
        Hash='4846'
        divide='4689'
        at='4897'
        percent='5956'
        power='7770'
        And='6097'
        asterick='9450'
        sub='5699'
        underscore='8944'
        equal='4455'
        add='4844'
        quest='9999'

        Coder=Coder.lower()
        for Code in Coder:
            if Code == "a":
                Output+=A
            if Code == "b":
                Output+=B
            if Code == "c":
                Output+=C
            if Code == "d":
                Output+=D
            if Code == "e":
                Output+=E
            if Code == "f":
                Output+=F
            if Code == "g":
                Output+=G
            if Code == "h":
                Output+=H
            if Code == "i":
                Output+=I
            if Code == "j":
                Output+=J
            if Code == "k":
                Output+=K
            if Code == "l":
                Output+=l
            if Code == "m":
                Output+=m
            if Code == "n":
                Output+=n
            if Code == "o":
                Output+=o
            if Code == "p":
                Output+=p
            if Code == "q":
                Output+=q
            if Code == "r":
                Output+=r
            if Code == "s":
                Output+=s
            if Code == "t":
                Output+=t
            if Code == "u":
                Output+=u
            if Code == "v":
                Output+=v
            if Code == "w":
                Output+=w
            if Code == "x":
                Output+=x
            if Code == "y":
                Output+=y
            if Code == "z":
                Output+=z
            if Code == " ":
                Output+=space
            if Code == "1":
                Output+=one
            if Code == "2":
                Output+=two
            if Code == "3":
                Output+=three
            if Code == "4":
                Output+=four
            if Code == "5":
                Output+=five
            if Code == "6":
                Output+=six
            if Code == "7":
                Output+=seven
            if Code == "8":
                Output+=eight
            if Code == "9":
                Output+=nine
            if Code == "0":
                Output+=zero
            if Code == ".":
                Output+=dot
            if Code ==",":
                Output+=comma
            if Code == "!":
                Output+=exclam
            if Code == "'":
                Output+=quote
            if Code == '"':
                Output+=Dquote
            if Code == ":":
                Output+=colon
            if Code == ";":
                Output+=semicolon
            if Code == "#":
                Output+=Hash
            if Code == "/":
                Output+=divide
            if Code == "@":
                Output+=at
            if Code == "%":
                Output+=percent
            if Code == "^":
                Output+=power
            if Code == "&":
                Output+=And
            if Code == "*":
                Output+=asterick
            if Code == "-":
                Output+=sub
            if Code == "_":
                Output+=underscore
            if Code == "=":
                Output+=equal
            if Code == "+":
                Output+=add
            if Code == "?":
                Output+=quest
        return Output

except KeyboardInterrupt:
    print("Cancelled")
