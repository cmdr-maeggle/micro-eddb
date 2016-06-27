/**
 * Some User Interface / User Experience improvement glue.
 */

+function ($) {
    var round = function (x, n) {
        var e = Math.max(1, Math.pow(10, n)); // make sure the expansion factor is at least "1"
        return Math.round(x * e) / e;
    };

    $(document).ready(function () {
        $(".table-sortable").tablesorter();

        $(".blueprint-effects dd").each(function() {
            $element = $(this);
            var data_gain = $element.data("gain") == "1";
            var range_min = parseFloat($element.find(".min").text());
            var range_max = parseFloat($element.find(".max").text());

            var data_min, data_max, bar_left, bar_width;

            if (data_gain) {
                data_min = (range_min != range_max) ? range_min : 0;
                data_max = range_max;
            } else {
                data_min = (range_min != range_max) ? range_max : 0;
                data_max = range_min;
            }

            bar_width = (range_max - range_min) * 100 * 0.5; // only 1/2 of the actual spread so we can fit in the -1->+1 bar
            if (data_gain) {
                bar_left = (range_min - 1) * 50 + 50;
            } else {
                bar_left = -((range_min - 1) * 50) + 50 - bar_width;
            }

            // scale bar and bar location if needed
            if (range_max >= 2) {
                var scale = 1 / ((range_max - 1 /* normalize to 0-position */) * 1.2 /* arbitrary factor for padding purposes */);
                bar_left = ((bar_left - 50) * scale) + 50;
                bar_width *= scale;
            }

            var $range_indicator = $("<div></div>").addClass("progress").append(
                $("<div></div>").addClass("progress-bar" + (data_gain ? "" : " progress-bar-danger")).attr({
                    'data-min': (data_min == 1) ? "" : round(data_min, 2),
                    'data-max': (data_max == 1) ? "" : round(data_max, 2),
                    'style': "margin-left: " + bar_left + "%; width: " + bar_width + "%"
                })
            ).append($("<div></div>").addClass("zero-indicator"));
            $element.append($range_indicator);
        });
    });
}(jQuery);