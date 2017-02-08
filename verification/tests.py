﻿"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [['000',
                       '120',
                       '000']],
            "answer": 6,
            "explanation":['100',
                           '110',
                           '111'],
        },
        {
            "input": [['00000',
                       '05670',
                       '04980',
                       '03210',
                       '00000']],
            "answer": 26,
            "explanation":['10000',
                           '11110',
                           '11110',
                           '11110',
                           '11111'],
        },
        {
            "input": [['000000001',
                       '222322222',
                       '100000000']],
            "explanation":['111111111',
                           '111111111',
                           '111111111'],
            "answer": 26,
        },
        {
            "input": [['000000002110',
                       '011100002310',
                       '012100002220',
                       '011100000000']],
            "answer": 26,
            "explanation":['100000000000',
                           '100000000111',
                           '111111110111',
                           '000000011111'],
        },
        {
            "input": [['00000000120000',
                       '00100002432100',
                       '01211111211000',
                       '00100000000000']],
            "answer": 18,
            "explanation":['11111111110000',
                           '00000000111111',
                           '00000000000001',
                           '00000000000001'],
        },
        {
            "input": [['00000000000000000000000000',
                       '00000000000111111100000000',
                       '00000000000122222100000000',
                       '00000000000123332100000000',
                       '00000000000123432100000000',
                       '00000000000123332100000000',
                       '00000000000122222100000000',
                       '00000000000111111100000000',
                       '00000000000000000000000000',
                       '00000111110000000000000000',
                       '00000122210000000000000000',
                       '00000123210000000000000000',
                       '00000122210000000011223110',
                       '00000111110000000000000000',
                       '01110000000000000000000000',
                       '01210000000000000000000000',
                       '01110000000000000000000000',
                       '00000000000000000000000000']],
            "answer": 70,
            "explanation":['10000000000000000000000000',
                           '10000000000000000000000000',
                           '10000000000000000000000000',
                           '10000000000000000000000000',
                           '10000000000000111110000000',
                           '10000000000000100010000000',
                           '10000000000000100010000000',
                           '10000000000000100010000000',
                           '10000000000000100010000000',
                           '10000000000000100010000000',
                           '10000000000000100010000000',
                           '10000001111111100010000000',
                           '10000001000000000011111000',
                           '10000001000000000001000000',
                           '10000001000000000001000000',
                           '11111111000000000001000000',
                           '00000000000000000001000000',
                           '00000000000000000001111111']

        },
     ]
}