//Dont change it
//Dont change it
requirejs(['ext_editor_io', 'jquery_190', 'raphael_210'],
    function (extIO, $, TableComponent) {

        function climbingRouteCanvas(dataInput, dataExplanation, result) {
            var zx = 10;
            var zy = 10;
            var cellSize = 26;
            var fullSizeX = zx * 2 + cellSize * dataInput[0].length;
            var fullSizeY = zy * 2 + cellSize * dataInput.length;
            var max_elv = 0;
            var colorDark = "#294270";
            var colorOrangeAry = [
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
            ];
            var colorBlueAry = [
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
            ];
            var attrRect = {"stroke": colorDark, "stroke-width": 1};
            var attrText
                = {"stroke": colorDark,
                    "font-size": 12, 
                    "font-family": "Verdana"};

            this.createCanvas = function (dom) {
                this.paper = Raphael(dom, fullSizeX, fullSizeY, 0, 0);
                for (var i = 0; i < dataInput.length; i++) {
                    for (var j = 0; j < dataInput[i].length; j++) {
                        var elv = dataInput[i].slice(j, j+1)*1;
                        this.paper.rect(zx + j * cellSize,
                            zy + i * cellSize,
                            cellSize,
                            cellSize).attr(attrRect).attr("fill",
                                result && dataExplanation[i].slice(j,j+1)*1 
                                    ? colorOrangeAry[elv]
                                    : colorBlueAry[elv]);
                        this.paper.text(zx + j * cellSize + cellSize / 2,
                            zy + i * cellSize + cellSize / 2,
                            String(dataInput[i].slice(j, j+1))
                        ).attr(attrText);
                    }
                }
                return false;
            };
        }
        var $tryit;
        var io = new extIO({
            multipleArguments: true,
            functions: {
                js: 'climbingRoute',
                python: 'climbing_route'
            },
            animation: function($expl, data){
                if (! data.ext.explanation) {
                    return;
                }
                var canvas = new climbingRouteCanvas(
                    data.in[0],
                    data.ext.explanation,
                    data.ext.result);
                canvas.createCanvas($expl[0]);
            }
        });
        io.start();
    }
);
