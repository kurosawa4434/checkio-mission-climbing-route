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
        { "input": [['000', '120',
                       '000']],
            "answer": 6,
            "explanation":' SEWSEE',
        },
        {
            "input": [['00000',
                       '05670',
                       '04980',
                       '03210',
                       '00000']],
            "answer": 26,
            "explanation": 'SSSSEEENWW' +
                           'NNEESWENWW' +
                           'SSEESE'
        },
        {
            "input": [['000000001',
                       '222322222',
                       '100000000']],
            "answer": 26,
            "explanation": 'EEEEEEEESW' +
                           'WWWWWWWSEE' +
                           'EEEEEE'
        },
        {
            "input": [['000000002110',
                       '011100002310',
                       '012100002220',
                       '011100000000']],
            "answer": 26,
            "explanation": 'SSEEEEEEESEEEENNWSWNSENESS'
        },
        {
            "input": [['00000000120000',
                       '00100002432100',
                       '01211111211000',
                       '00100000000000']],
            "answer": 18,
            "explanation": 'EEEEEEEEESWEEEEESS'
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
            "explanation": 'ESSSSSSSSS' +
                           'SSSSEEEENN' +
                           'NNEEEEEENN' +
                           'NNNNEEEESS' +
                           'SSSSSEWSSS' +
                           'SE'
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
            "explanation": 'EEEEEESSSN' +
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
            "explanation": 'SEEEEENSSS' +
                           'SEEEEWWWSS' +
                           'SSSSENEESN' +
                           'WWSSWSSSEE' +
                           'EEE'
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
            "explanation": 'SSSSSSSSSE' +
                           'EEEEEEEEEE' +
                           'EEENWNWESE' +
                           'SSSSSEE'
        },
    ],

}
