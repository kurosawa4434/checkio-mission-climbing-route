"""
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
            "explanation": {
                "cell_size": 50,
                "font_size": 26,
                "route": ' SEWSEE',
            }
        },
        {
            "input": [['00000',
                       '05670',
                       '04980',
                       '03210',
                       '00000']],
            "answer": 26,
            "explanation": {
                "cell_size": 40,
                "font_size": 18,
                "route":
                    'SSSSEEENWW' +
                    'NNEESWENWW' +
                    'SSEESE',
            }
        },
        {
            "input": [['000000001',
                       '222322222',
                       '100000000']],
            "answer": 26,
            "explanation": {
                "cell_size": 26,
                "font_size": 12,
                "route":
                    'EEEEEEEESW' +
                    'WWWWWWWSEE' +
                    'EEEEEE'
            }
        },
        {
            "input": [['000000002110',
                       '011100002310',
                       '012100002220',
                       '011100000000']],
            "answer": 26,
            "explanation": {
                "cell_size": 26,
                "font_size": 12,
                "route":
                    'SSEEEEEEES' +
                    'EEEENNWSWN' +
                    'SENESS'
            }
        },
        {
            "input": [['000000120000',
                       '001002432100',
                       '012111211000',
                       '001000000000']],
            "answer": 16,
            "explanation": {
                "cell_size": 26,
                "font_size": 12,
                "route":
                    'EEEEEEESWE' +
                    'EEEESS'
            }
        },
        {
            "input": [['00000000111111100',
                       '00000000122222100',
                       '00000000123332100',
                       '00000000123432100',
                       '00000000123332100',
                       '00000000122222100',
                       '00000000111111100',
                       '00011111000000000',
                       '00012221000000000',
                       '00012321000000000',
                       '00012221000000012',
                       '00011111000000000',
                       '11100000000000000',
                       '12100000000000000',
                       '11100000000000000']],
            "answer": 52,
            "explanation": {
                "cell_size": 20,
                "font_size": 10,
                "route":
                    'ESSSSSSSSS' +
                    'SSSSEEEENN' +
                    'NNEEEEEENN' +
                    'NNNNEEEESS' +
                    'SSSSSEWSSS' +
                    'SE'
            }
        },
    ],
    "Extra": [
        {
            "input": [['0000000000000',
                       '0232021202320',
                       '0222022202220',
                       '0212023202120',
                       '0000000000000',
                       '0232021202320',
                       '0222022202220',
                       '0212023202120',
                       '0000000000000',
                       '0232021202320',
                       '0222022202220',
                       '0212023202120',
                       '0000000000000']],
            "answer": 110,
            "explanation": {
                "cell_size": 26,
                "font_size": 12,
                "route":
                    'EEEEEESSSN' +
                    'NNWWSSSSWW' +
                    'NNNSSSEEEE' +
                    'SSSNNNEEEE' +
                    'NNNSSSEESS' +
                    'SSWWNNNSSS' +
                    'WWWWSSSNNN' +
                    'WWWWNNNSSS' +
                    'WWSSSSEENN' +
                    'NSSSEEEEEE' +
                    'EENNNSSSEE'
            }
        },
        {
            "input": [['000002000000',
                       '000001000000',
                       '000000000000',
                       '000001002220',
                       '000001012320',
                       '000001002220',
                       '000001000000',
                       '000001000000',
                       '000001000000',
                       '000001022220',
                       '000001120320',
                       '000001120020',
                       '000001022220',
                       '000001000000',
                       '000001000000']],
            "answer": 43,
            "explanation": {
                "cell_size": 26,
                "font_size": 12,
                "route":
                    'SEEEEENSSS' +
                    'SEEEEWWWSS' +
                    'SSSSENEESN' +
                    'WWSSWSSSEE' +
                    'EEE'
            }
        },
        {
            "input": [['01220000122332332',
                       '12343000023443211',
                       '11232100000232100',
                       '11110000001223121',
                       '11011002223333443',
                       '21002023334454564',
                       '10000234556678752',
                       '10000046778898531',
                       '10000004555677642',
                       '11000000001234532',
                       '22112211000123421',
                       '11234432210002321',
                       '22345443321012210',
                       '33456554332111210']],
            "answer": 37,
            "explanation": {
                "cell_size": 20,
                "font_size": 10,
                "route":
                    'SSSSSSSSSE' +
                    'EEEEEEEEEE' +
                    'EEENWNWESE' +
                    'SSSSSEE'
            }
        },
        {
            "input": [['01020',
                       '00304',
                       '05060',
                       '00708',
                       '00000']],
            "answer": 8,
            "explanation": {
                "cell_size": 40,
                "font_size": 18,
                "route":
                    'SSSSEEEE'
            }
        },
        {
            "input": [[
                '00000000000',
                '00000100000',
                '00000200000',
                '00022322000',
                '00023432000',
                '01234543210',
                '00023432000',
                '00022322000',
                '00000200000',
                '00000100000',
                '00000000000',
            ]],
            "answer": 20,
            "explanation": {
                "cell_size": 20,
                "font_size": 10,
                "route":
                    'EEEEESSSSSSSSSSEEEEE',
            }
        },
    ],
}
