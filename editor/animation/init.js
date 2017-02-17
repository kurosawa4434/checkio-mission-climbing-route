//Dont change it
requirejs(['ext_editor_io', 'jquery_190', 'raphael_210'],
    function (extIO, $, TableComponent) {

        function climbingRouteCanvas(
            dom, dataInp, dataExp, result) {
            var zx = 10;
            var zy = 10;
            var cellSize = 26;
            var fullSizeX = zx * 2 + cellSize * dataInp[0].length;
            var fullSizeY = zy * 2 + cellSize * dataInp.length;
            var max_elv = 0;
            var color = {
                dark: "#294270",
                orange: [
                    "#FABA00",
                    "#FAB500",
                    "#FAB000",
                    "#FAAC00",
                    "#FAA700",
                    "#FAA200",
                    "#FA9D00",
                    "#FA9900",
                    "#FA9400",
                    "#FA8F00",
                ],
                blue: [
                    "#8FC7ED",
                    "#7FBDE5",
                    "#6FB3DE",
                    "#5FA9D6",
                    "#4F9FCF",
                    "#4094C7",
                    "#308AC0",
                    "#2080B8",
                    "#1076B1",
                    "#006CA9",
                ]
            };
            var attrRect = {"stroke": color.dark, "stroke-width": 1};
            var attrText
                = {"stroke": color.dark,
                    "font-size": 12, 
                    "font-family": "Verdana"};

            var paper = Raphael(dom, fullSizeX, fullSizeY, 0, 0);
            var cell_dic = paper.set();
            var text_dic = paper.set();
            var phase = 0;
            for (var i = 0; i < dataInp.length; i++) {
                for (var j = 0; j < dataInp[i].length; j++) {
                    var elv = dataInp[i].slice(j, j+1)*1;
                    var cell= paper.rect(zx + j * cellSize,
                        zy + i * cellSize,
                        cellSize,
                        cellSize).attr(attrRect).attr("fill",
                            color.blue[elv]);
                    var text = paper.text(zx + j * cellSize + cellSize / 2,
                        zy + i * cellSize + cellSize / 2,
                        dataInp[i].slice(j, j+1)
                    ).attr(attrText);

                    cell_dic[i*100+j] = cell;
                    text_dic[i*100+j] = text;
                }
            }
            var [x, y] = [0, 0];
            var path_dic = {};
            dataExp = ' ' + dataExp;
            for (var i=0; i < dataExp.length; i+=1) {
                var dir = dataExp.slice(i, i+1);
                var em = 0;
                switch(dir){
                    case 'N': y -= 1; break;
                    case 'S': y += 1; break;
                    case 'W': x -= 1; break;
                    case 'E': x += 1; break; 
                }
                var elv = dataInp[y].slice(x, x+1)*1;
                var co = y*100 + x;
                if (path_dic[co] === undefined){
                    path_dic[co] = 0;
                } else {
                    path_dic[co] += 3;
                }
                setTimeout(function () {
                    var c = co;
                    var e = Math.min(elv + path_dic[co], 9);
                    return function(){
                        cell_dic[c].animate({'fill': color.orange[e]}, 50);
                    };
                }(), 50 * (phase));
                phase += 1;
            }
            return false;
        }

        var $tryit;
        var io = new extIO({
            multipleArguments: true,
            functions: {
                js: 'climbingRoute',
                python: 'climbing_route'
            },
            animation: function($expl, data){
                climbingRouteCanvas(
                    $expl[0],
                    data.in[0],
                    data.ext.explanation,
                    data.ext.result
                );
            }
        });
        io.start();
    }
);
