//Dont change it
requirejs(['ext_editor_io', 'jquery_190', 'raphael_210'],
    function (extIO, $, TableComponent) {
        function climbingRouteCanvas(dom, dataInp, dataExp, result) {
            const [zx, zy] = [10, 10]
            const cellSize = dataExp.cell_size
            const fullSizeX = zx * 2 + cellSize * dataInp[0].length
            const fullSizeY = zy * 2 + cellSize * dataInp.length
            const color = {
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
            }
            /*------------------------------------------------*
             *
             * attr
             *
             *------------------------------------------------*/
            const attr = {
                rect: {
                    'stroke': color.dark,
                    'stroke-width': 1
                },
                text: {
                    'font-size': dataExp.font_size,
                    'font-family': "Verdana"
                },
                text_color: {
                    'zero': {
                        'stroke': '#8FC7ED',
                        'fill': '#8FC7ED',
                    },
                    'others': {
                        'stroke': color.dark,
                        'fill': color.dark,
                    },
                },
            }

            /*------------------------------------------------*
             *
             * draw cell & text
             *
             *------------------------------------------------*/
            const paper = Raphael(dom, fullSizeX, fullSizeY, 0, 0)
            const cell_dic = paper.set()
            const text_dic = paper.set()
            for (let i = 0; i < dataInp.length; i+=1) {
                for (let j = 0; j < dataInp[i].length; j+=1) {
                    const ev = dataInp[i].slice(j, j+1) * 1

                    // cell
                    cell_dic[i*100+j]
                        = paper.rect(zx + j * cellSize,
                            zy + i * cellSize,
                            cellSize,
                            cellSize).attr(attr.rect).attr("fill",
                                color.blue[ev])

                    // text
                    text_dic[i*100+j]
                        = paper.text(zx + j * cellSize + cellSize / 2,
                            zy + i * cellSize + cellSize / 2,
                            ev
                        ).attr(attr.text).attr(
                            ev === 0 ? attr.text_color.zero
                                    : attr.text_color.others)
                }
            }

            /*------------------------------------------------*
             *
             * paint route
             *
             *------------------------------------------------*/
            let [x, y] = [0, 0]
            let path_dic = {}
            const route = (' ' + dataExp.route).split('')
            let n = 0

            function paint_route() {
                if (n >= route.length) {
                    return
                }

                switch(route[n]) {
                    case 'N': y -= 1; break;
                    case 'S': y += 1; break;
                    case 'W': x -= 1; break;
                    case 'E': x += 1; break;
                }

                const ev = dataInp[y].slice(x, x+1) * 1
                const co = y * 100 + x

                if (path_dic[co] === undefined){
                    path_dic[co] = 0
                } else {
                    path_dic[co] += 3
                }

                n += 1
                const e = Math.min(ev + path_dic[co], 9)
                text_dic[co].animate(attr.text_color.others)
                cell_dic[co].animate({'fill': color.orange[e]}, 20, paint_route)
            }

            paint_route()
            return false
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
