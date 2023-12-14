import math

input = [
    "BBFFBFBRLL",
    "FFFFBFBRLR",
    "BFFBBFBRLR",
    "BFBBBFBLLL",
    "FFBBFBBLRR",
    "BFBFFFFRRL",
    "BBBBFFFRLR",
    "BFFFBBFRLL",
    "FFFFBFBRRL",
    "BFBBFFFRRL",
    "BBFBBBFRLL",
    "FBFFBFFRLL",
    "FBBBBBBLRL",
    "FFFBBFBLRL",
    "FFBBFFFLLR",
    "FBBFFFBLLL",
    "FFBFBBBRRL",
    "FBFBBBFRRL",
    "FFBBBFFLRL",
    "BFBBBBFRLR",
    "FBBBFFBRRL",
    "FBBFBFFRLL",
    "FBFBFBBLLL",
    "BFBFFFFLRR",
    "FFFBBFFLLL",
    "FFFFBFFRLL",
    "FBBBBFBRRR",
    "FBBFBBBLRL",
    "BBBBFFFLLL",
    "FFFFBFBLLR",
    "BFFFFBBRLL",
    "BFFFFBBRLR",
    "BFFFFFBRLL",
    "BFFBBBFRRL",
    "FBFFBBBLRR",
    "BFBFFBFRRR",
    "BBBBFFBLRR",
    "FFFFFBBRLR",
    "BFFFBBBRLR",
    "BBFBFFBRRL",
    "FBBFBFBLRR",
    "BFBBFBFRLR",
    "FFFFFBFRRR",
    "BFFFFFBLRL",
    "FFFBFBBLLR",
    "BFFFBBBLRR",
    "FFBFFBBRRL",
    "FBBBBBBLLL",
    "FBBBBFBLRL",
    "BBFFFBFRRL",
    "BBFFFBBRRL",
    "FFBFBFBLRL",
    "FFFFBBBRLR",
    "FBBFFBFLRL",
    "FBBBBFBRLR",
    "BBFBFBBLRL",
    "BBBBFFFLRR",
    "BFBBFFBRLL",
    "BFBBFBBRLR",
    "FFFBBFBRRR",
    "BFFBBBFRRR",
    "BFBBFBBLRR",
    "FBBFFBBLRL",
    "FFFBFBBRRL",
    "BFFFBFBRRR",
    "FBBBFFBLRR",
    "BBFFBBBLLR",
    "BFFBBBBRLR",
    "BBBBFBFRRR",
    "BBBBFFFRRL",
    "BBFFBBBRRL",
    "FFBBBBBRRL",
    "FFFFBBFRRL",
    "BFFFFFBLLL",
    "FFBFFBBLRL",
    "FFFBBFFLRL",
    "BFBFBFFLLR",
    "FFFFBFFRRL",
    "FBBBBFFRLR",
    "FBBBBFBRRL",
    "FBBBFBFLLR",
    "FBBBBBBRRR",
    "FBBFFFFRRL",
    "FBFBFFFRLL",
    "BBFFFBFRLL",
    "BFFBFFFRLL",
    "FFFFBFFLRL",
    "FBBFFFFLLR",
    "BBBBFFBRLL",
    "FBFBFBBRLL",
    "BBFBBBFLLL",
    "FFBFBBBRRR",
    "BFBBFBFRRR",
    "BFBFBBFLRR",
    "BBFBBBFLRL",
    "BBFFFBBLRL",
    "FBFFFBFRLR",
    "FFBFFBBRLL",
    "FFBFFBFRLR",
    "BBBFBFFLLR",
    "BBFBFBBLRR",
    "FBBBBFFLLR",
    "BFFBFBFLRL",
    "FFFBFFFLRR",
    "FBBFBBBRRL",
    "FBFBBBBRRL",
    "BFBFBBFLLL",
    "BFBFBBFRLL",
    "FBFBFFBLLR",
    "FBFFFFBRLR",
    "BBFBBBFRRL",
    "BBBFFFFLLL",
    "FFFFBFBLRL",
    "FFBFFFBLLR",
    "FFFBBBBRRL",
    "FFBFFFBLRL",
    "BBBBFBFRRL",
    "FFFBFFFLLR",
    "BBBBFBBRLR",
    "BBFBBBBRRL",
    "FBFBFFBRLL",
    "FBBBFBFRLL",
    "BFFBFBBRLR",
    "FBFBFBBLRR",
    "FBBFFFBLRR",
    "FFFBBFFRLR",
    "BBBFFFBRLR",
    "BBFFBFFLLL",
    "BFFFFBBLLR",
    "BFBFBBFLRL",
    "FFBFBFBRLL",
    "FBBFBFBRRL",
    "BBBFBFFLLL",
    "FFBBFFFRRR",
    "BFFBBFBLLL",
    "BBBFFBFLLR",
    "FFFBFBBLLL",
    "FFBFBFFRLL",
    "BFFBBBBLRL",
    "FBFBBFFLRL",
    "FBFFBFBLRL",
    "BFBBBBFLRR",
    "BBBFBFFRRR",
    "FBFBBFFRLR",
    "BFBBFFFLLR",
    "BFFFBFBLRR",
    "FBFBFBBRLR",
    "FFFFFBFRLR",
    "FFFFBBBRRL",
    "FBBFFBFLLL",
    "FBBBBBBRLR",
    "FBBFFFBRLR",
    "FBBBFBBRLL",
    "FFFBFBFRLL",
    "BFBFBBFLLR",
    "FFBFFBFRRL",
    "BBFBBBFRLR",
    "FFBBBBBLRL",
    "BBFBBFBRLL",
    "FFBFFFBRLL",
    "FFBBBFFRLR",
    "BFFBBBFLRL",
    "FFBFBFBRRL",
    "FBBFFFBRRR",
    "BBFBBFFLLL",
    "FBFFFFFRLL",
    "FBFFFFBLRL",
    "FFFBFFBRRR",
    "BBBFBFBRLL",
    "BBBBFBBRLL",
    "BFFBFBBLLR",
    "BBBFFFBLRL",
    "BFFBFFBRLL",
    "BFFBBFBRRL",
    "FBFFFFFRRL",
    "FFBBFBBRRR",
    "BBFFBBFLLR",
    "FFBFFBBLRR",
    "BBBFBFFLRL",
    "BBBBBFFLLL",
    "FFBBBBBLRR",
    "BFFBFFBRLR",
    "BFFBBFBLRL",
    "BBFFBBFRRL",
    "FFFBFFBRLR",
    "BFBFBBBLLR",
    "BFFBFFFLLL",
    "FBBFBBBRLR",
    "BFBFBBBRRL",
    "FBFBFFBRRL",
    "BBBFBFBLRL",
    "BFFFBBBLLR",
    "FBBBFBFLRR",
    "FFBBBBBRLR",
    "FFBFFBBLLL",
    "BBFFBFBLRL",
    "BFBFBFBRRL",
    "BFBFFBFLRR",
    "FFBBBFBLLR",
    "BFBFBBBRRR",
    "FBFFBBFLRR",
    "BBBFBFFRLR",
    "BFFFFBFRLL",
    "FFFFBBFLRL",
    "FBBBBFBLLR",
    "BFBFFFFLLR",
    "FFBBFBBRLL",
    "FBFBBFFRRL",
    "BFFFBBFLRR",
    "BBBFFBFLRR",
    "FBBBFFFLRR",
    "BBFFFBFRLR",
    "FFFBFBBRLR",
    "FFBBFBBLRL",
    "FBFFBBBRRR",
    "BBFBBBBLLR",
    "BFFFFFBRLR",
    "BBFBFBFRLR",
    "FBFBBBFLRR",
    "BBFFFBBLLL",
    "BBBFBFBLLR",
    "BFFBBFFLRL",
    "FFBFFFFRLR",
    "BFFFFFBRRR",
    "FFBBBFBLRR",
    "BBBFBBBLRR",
    "BBBBBFFLRL",
    "FBFFFBFRRR",
    "BFFFFFBLLR",
    "FFBBFBFLRL",
    "BBFFFBFRRR",
    "BBBFBFBRLR",
    "BBFBBFBLRL",
    "FFFBFFBLRL",
    "FFFBFFBRLL",
    "BBBBFFFRLL",
    "FBBFFFFLRR",
    "FFBBFFBLLR",
    "FBFFBFBRLL",
    "FFBFBFFLLL",
    "BFBBFFBLRR",
    "BFBFFFBRLR",
    "BBBFFBFRRL",
    "FFBBFBBRLR",
    "BBFFFFBRLL",
    "BBFFBFBLLR",
    "BBFFBFBRRL",
    "FBBBFBBRRL",
    "FFFFFBBRLL",
    "FBFFFBFRRL",
    "FBBFBFFLRL",
    "FBFBBBFRLL",
    "BFFFBFFLRR",
    "BFFBBFBRRR",
    "BFBBFBBLLL",
    "BBFBFFFLRL",
    "BFBFFFFRRR",
    "FBBFBBBLRR",
    "FFBBBBBLLR",
    "FFFFBBFRRR",
    "FFBBFFBRRR",
    "BBFFFBBLLR",
    "BFFBFFBLLR",
    "BBBFFFFRLL",
    "FFFBFBFLLR",
    "BBFBFFBLRL",
    "FFBBBFBRRL",
    "BBFBBBBRRR",
    "BBFBBFBRRR",
    "FFFFBFBRLL",
    "FFFBFFBLLR",
    "FFBFBBBLLR",
    "FBBBFBFLRL",
    "BFBBBBBLLL",
    "BFBBFBFRLL",
    "BFBFBBBLRR",
    "FFBFBFBLLL",
    "BFBFFFBLLR",
    "BBBBFBBRRL",
    "FFBFFBFLRR",
    "FBFBBFFLLL",
    "BFBFBBBRLL",
    "BFBFFFBRRR",
    "FBBFBBFRRR",
    "BFFBFBFRLL",
    "BBFFFFBRRL",
    "BFBFBFBLRL",
    "FBBBFFBRRR",
    "FFFFBBBLLR",
    "BBBFFFFRRR",
    "BBBFFFFLRR",
    "FFBFBBFLLL",
    "BFBFBFFRRR",
    "BBFFFBBRLR",
    "FBBBBBFLRR",
    "FBFFBFBLLR",
    "FFBFFFBLLL",
    "BFFFFBBLRL",
    "BBBFBBBRRR",
    "BBBFFFBRRL",
    "BFFFFBBLRR",
    "BBFFBBBRLL",
    "BFBFFFFLRL",
    "BBFFFFFLRR",
    "BBFFFBFLRR",
    "FBFFBBFRRL",
    "BFFFBBBLLL",
    "BFBBBFFRRL",
    "BFFFBFBLRL",
    "FBBBBFFRLL",
    "BFBFBBBLLL",
    "BFBBFFBLLR",
    "BBBBFBBLLL",
    "FBFBFBFLRR",
    "FBBBFFFRLR",
    "BFFBFBFRRL",
    "BFBBFFFRLR",
    "FBBBFFFLRL",
    "FBBBBFFLRR",
    "FBFFFFBLLL",
    "BBBFFBBRLL",
    "FBBFBFFLLL",
    "BFFBBFBRLL",
    "BFFFFBFRLR",
    "FFFBBFFRRR",
    "FFFBBBFRLR",
    "FBBFFBFRRR",
    "FBFFFFBRRR",
    "BFBFBFBRLL",
    "BBBBBFFRLL",
    "BFFFFBFLLL",
    "BBFFBBFRRR",
    "BFBFFFBLLL",
    "FFFBFBFRRR",
    "FBFBBFBRRL",
    "BFBFFFBRRL",
    "FFFBBBBRRR",
    "BFBFFBBLLR",
    "FBBBFBBLLR",
    "BBFBBFBLLR",
    "BFFFFFFLLL",
    "FBBFBFFRLR",
    "FFBBBBFLLL",
    "BFBBFBFLRL",
    "BFBFBFBLLL",
    "FBBBFBBLLL",
    "BFBFBFBRRR",
    "FBFBFFFLRR",
    "FBFBBFBLLL",
    "FBFFFFBLRR",
    "BBBFFBFRLL",
    "FFFBFFBRRL",
    "BBFBFBFRRR",
    "FBBFFBFRLL",
    "BBBFBBFRRR",
    "FBFBBFFLRR",
    "BBFBBBBLLL",
    "FFBFFBBLLR",
    "FBBBFFFRRR",
    "FFFFFBBLLL",
    "FBFFBBBRRL",
    "BFFBBBFRLL",
    "BFFFBFFLLR",
    "FBFFBBBLLL",
    "FFFBBBBRLR",
    "BFBBBFFLLR",
    "FBFBBBBLLR",
    "FBBFBFBRRR",
    "BBFFBFFRRR",
    "FBBFFFFLRL",
    "FBFBBBBLRR",
    "FFBBFBFRRR",
    "FBFBBFBRLR",
    "BBFBFBFRRL",
    "FBBBBBFLLL",
    "FBFFBFFLLR",
    "FBFBFBFLLL",
    "BFFBFBFLRR",
    "FBBBBBFRLL",
    "BFFBBBFRLR",
    "BBFFFFFLLL",
    "FFFFBBFRLR",
    "BFBBBBBLLR",
    "BBFFFBBRLL",
    "FBFFFFFLRR",
    "BBBFFBBRRR",
    "FFFBFFBLRR",
    "BFFFFFFRLL",
    "BBFFFBFLLR",
    "BFFBBFFLLL",
    "FBBBFFFRRL",
    "BBBBFBFLLL",
    "FBBFFFFRLL",
    "FBFBBFBRRR",
    "BFFFFFFRLR",
    "BFBFFFFLLL",
    "FBFBBFBLLR",
    "BFBBFBFLLR",
    "BFBBFBBLRL",
    "BFFFBFFRLR",
    "BBFBBFFRRR",
    "FBFBFBFRLL",
    "FFBBFBFRRL",
    "BFFFBFFLRL",
    "FBFFBBBLRL",
    "BBBFFBFLRL",
    "FFBBBFBRRR",
    "BFFFBFBRRL",
    "FFBBFBFLLR",
    "BFFBFFFLRL",
    "BBBFFFFLRL",
    "FFBBFFBRLR",
    "BFFBFBBRRR",
    "BFFBFFBLRR",
    "BFFFBBBLRL",
    "FFBFBFFRRR",
    "FFBFBBFRRL",
    "FFBBBBFRLR",
    "BBBFBBFLRR",
    "BFBBFFFLRL",
    "BFBBBBFRRR",
    "FFBFFFBLRR",
    "FFBFBFFLLR",
    "FBFFBFBRRL",
    "BFFFFFFLRR",
    "FBBBBBBLRR",
    "BBFFBBFLLL",
    "BFBBBBFRRL",
    "FFBFFFFLLR",
    "BBFFFBFLLL",
    "FFBFBFFLRR",
    "FFBBBBFLRL",
    "FFFBBBFRRR",
    "FBBFFBFLRR",
    "FBFBBBBRLL",
    "FFFBBBBLLL",
    "FFBBBBFRRL",
    "FBBBBBBLLR",
    "FBBFBFFLLR",
    "BFBBFBFRRL",
    "BBFFBFBLRR",
    "FBFFBFFRRR",
    "FFFBBBBRLL",
    "BFFFFFFLLR",
    "BFFFFBFLLR",
    "FFFBBBFRRL",
    "BFFBFFFLLR",
    "FBFFFFFLLL",
    "BBBBFBBLRR",
    "BBFFBFFRRL",
    "BFBBFFBLRL",
    "FBBBBFFRRR",
    "FFFBBFBLLR",
    "FBBFFFFRLR",
    "FFFBFBBLRL",
    "BFBBBBFLLR",
    "BBFFFBBRRR",
    "BFBFBBFRRR",
    "FFFBFFFRRL",
    "BBFBFBFRLL",
    "FBFFBFFRLR",
    "BFFBFFBLLL",
    "FFFFBFBRRR",
    "BFFBBFFRLR",
    "FBBBFBBLRL",
    "FBFFBBBRLL",
    "FBBBBBFRLR",
    "FBBBFFBLLR",
    "FBFBBFFRLL",
    "FFBBBFFRRL",
    "BBFBBBBLRR",
    "BFFFFBBRRL",
    "BFFFBFFRRL",
    "FBBFBBFRRL",
    "BFBBFFBRLR",
    "BFFFFBFLRL",
    "BBFFFFBLLR",
    "FBFFFFFRRR",
    "FFFFBBBRLL",
    "FFFFBBFLLR",
    "BBBFBBBLLR",
    "FFBFFFFRLL",
    "FBBBFFFLLR",
    "FFFFBBBLRL",
    "FBFBBBFLLL",
    "FBFFFBFLLL",
    "BBBFFBBLRR",
    "FBBBFFFLLL",
    "BBFBBFFRLR",
    "FFFFBFFLLL",
    "BBFFBFFLLR",
    "BFBBBBFRLL",
    "BFFBBFFRLL",
    "BBFFFFBRLR",
    "FBBBBFBRLL",
    "BFBBFFBLLL",
    "FBBFFFFLLL",
    "FFBFFBBRRR",
    "FBFFBBBLLR",
    "BFBBBFBLRL",
    "BBFFBBFRLR",
    "FFBBBFFRRR",
    "BBBBFBFRLL",
    "BFFFBBBRRR",
    "BBFFFFFRLR",
    "FBFBFFFLLR",
    "BBFFBBFRLL",
    "BFFBBFFLLR",
    "FFFFBBBRRR",
    "FFFBFBFRRL",
    "BBBFBBFRRL",
    "FBBBFBBRLR",
    "FBFBFFFRRR",
    "BFFBBBBLLR",
    "BBBFBFBLRR",
    "FBFBBFBLRR",
    "BBBFFBBRLR",
    "FBFBFBBLRL",
    "BBBFFBBLLR",
    "BBFBFBBRLL",
    "FBBBFFBRLL",
    "FFBBFFFRLL",
    "FBFFBFFRRL",
    "BBBBFFBRRR",
    "FBFBFFFLLL",
    "FFFFBBFRLL",
    "BFFBFFFRRR",
    "BBFFBFBRLR",
    "FFBBBFBRLL",
    "BBFBFFFLLL",
    "FBBFBBFRLR",
    "FFFBFFFRLL",
    "FBBFFBFRRL",
    "BFBFFBFLRL",
    "BBBFFFFRRL",
    "BBFFBBBRRR",
    "FFBFBFFRLR",
    "FFBBFFFRLR",
    "FBFBFBBRRL",
    "FFBBFBBLLR",
    "FBFFFFFRLR",
    "BBBBFBBLRL",
    "BBFFBFFRLL",
    "FBBBFBFLLL",
    "BBBFBFBLLL",
    "BFFBFFFLRR",
    "BFBFFBFRLL",
    "BFBBBBFLRL",
    "BBBBFFFLRL",
    "FFFBFFBLLL",
    "FFFFBFBLRR",
    "FFFFFBBRRR",
    "FFFBFBBLRR",
    "BFFFBBFRRL",
    "FFBFBBFLRR",
    "BBFBBBBRLL",
    "FBBBBBFRRR",
    "BFFFFBFLRR",
    "BFBFFBBRRL",
    "FBFBBFBLRL",
    "BBBFFBBLLL",
    "FFBBBFFLRR",
    "BBBBFBFLRL",
    "BBBBFFBLLL",
    "BFFFBBBRLL",
    "FBBFFFBLLR",
    "BFBBBFFRLL",
    "FBBFFBFRLR",
    "BBFBBFBRRL",
    "BFBBFBBRLL",
    "BBFBFFFRRR",
    "FBBBFFBRLR",
    "BBFFBBBLLL",
    "BFFFBFBLLR",
    "BBFBFFBRLR",
    "FFBFFFBRRL",
    "FFBFBFBRLR",
    "BBFFBFBLLL",
    "BFBFBBBRLR",
    "FBFFFBFLRL",
    "BFBFFFFRLR",
    "BBFFFFFRLL",
    "BBBFFFBRRR",
    "FBFFBBFRRR",
    "FFFBBFFLLR",
    "FFFBFBFRLR",
    "FFBBBBFLRR",
    "BFFFBFBRLR",
    "FFBFFBBRLR",
    "FBBFFFBRLL",
    "FBBFBFFLRR",
    "BFFFFFFRRR",
    "BBBFBBBRLL",
    "FBFFFBBRRL",
    "FFBBBFBLRL",
    "FBFFBFBLLL",
    "FFFFBFFRLR",
    "FBFFBFFLRL",
    "FFBFBFFRRL",
    "FBBBFFBLLL",
    "BFFFFBBRRR",
    "BBBBFFBLLR",
    "FFFFFBBLRL",
    "FFBBBFFLLR",
    "FBBBFFFRLL",
    "FFBFFBFRRR",
    "BBBBFFBRLR",
    "FFBBFBFLRR",
    "BFBBBBBRLL",
    "BFBBBBBLRL",
    "FFBFBBFRLR",
    "FFBFBBBRLL",
    "BFFBBFBLLR",
    "BFBFFFFRLL",
    "BBFBBFFRRL",
    "BFBFFBFRLR",
    "FFBBFFFLRL",
    "FFBBBFFLLL",
    "BFFBFBFLLL",
    "BFBFBFBRLR",
    "FBBFBFBLLR",
    "BFBFFBBLRR",
    "FFFFBFFLRR",
    "BBFBBFBLLL",
    "FBFFFFFLRL",
    "BBBBFBFRLR",
    "BFFFBBFRRR",
    "BBFBBFFLRR",
    "BFBBBFBRLL",
    "BFFBFFBLRL",
    "BFBFFFBLRR",
    "BFFFBFFRRR",
    "FBFFFBBLLL",
    "FBFBBBBLRL",
    "FBFBFFFRLR",
    "BBFFBBFLRL",
    "BFBFBFBLLR",
    "FBFFFBFLRR",
    "BFFBFBBRRL",
    "FBFBBBFLLR",
    "FBFBFFBLRL",
    "BBFBFBBRRR",
    "FBBFFBBLRR",
    "BBFFFFBLLL",
    "FBFFBBBRLR",
    "FBFFFBFLLR",
    "BFBBFFFLLL",
    "BBBBFBFLRR",
    "BFFBFBBRLL",
    "BFFFFFFRRL",
    "BFBFBFFRRL",
    "FFBFBFBLRR",
    "FFFBFBFLRR",
    "FFFBFBBRRR",
    "FBFFFBBRLR",
    "FFBBFFBRRL",
    "BBFBBBBRLR",
    "FFFBBFBRLR",
    "FBFFBBFLRL",
    "BBBFFFBRLL",
    "BBBFBBBRLR",
    "FFBFFFFRRR",
    "FBBFBFBLLL",
    "BFBBBFBRRR",
    "BFBBFFBRRL",
    "FFFBBBFLLL",
    "FBBBBFBLLL",
    "FFBFBFBLLR",
    "BFFBFFFRLR",
    "BBBBFBFLLR",
    "FBBFBBFLLL",
    "FBFFFBBLRR",
    "FFBFBBFRRR",
    "FBFBFBBRRR",
    "FFBFBFBRRR",
    "FFBBFBFRLL",
    "FBFBBBBLLL",
    "BFBFFBBLLL",
    "BBBFFFFRLR",
    "BBBFBFBRRR",
    "BFBFBFBLRR",
    "BFBFBBFRLR",
    "BFBBBFFLLL",
    "FBBFFBBRRR",
    "BFFFFFBLRR",
    "BFFBFBFRLR",
    "BBFFBFFRLR",
    "BFBBBBBLRR",
    "FBFFFBBLRL",
    "BFFBFBFRRR",
    "BFFFFBFRRL",
    "FFBFBBBLLL",
    "FBBBFBFRLR",
    "FFFBBFBLLL",
    "FBFBBBFRLR",
    "BFBFFFBRLL",
    "BFFBBBBLRR",
    "BBFFBFFLRL",
    "BBBFBBFRLL",
    "BBBFFFBLRR",
    "FBBFFBBRLR",
    "FBBFBBFLRR",
    "BBFBFBBRRL",
    "FFBBBBBLLL",
    "BFBBFBBLLR",
    "BFBBBFFLRR",
    "BBBFFFBLLL",
    "FBFBBBBRLR",
    "FBFBFFBLRR",
    "FFFBBBFLRL",
    "BBBFFBBLRL",
    "FBBFBFBRLL",
    "BBBBFBBLLR",
    "FFBBBBBRRR",
    "BBBFBBFLRL",
    "BFBBBFBRLR",
    "FFFBFFFRRR",
    "BFFFBBFRLR",
    "FBFFFFBRLL",
    "BFFBFFBRRL",
    "BBBFBBBRRL",
    "FFBFFBFRLL",
    "FBFBBFFRRR",
    "FFBFFFBRLR",
    "FFFFBFFLLR",
    "FFBBFFFLLL",
    "FBFFFBBLLR",
    "FFBFBBFLRL",
    "BFFBFBBLLL",
    "FBBBFBBLRR",
    "FFFBFBFLLL",
    "FBBFBFBLRL",
    "FFBBFFFRRL",
    "BFBFBFFRLL",
    "BFFFFBFRRR",
    "BBBBFFFRRR",
    "BFFBFFBRRR",
    "FFFFBFFRRR",
    "FFBBFBBRRL",
    "FBBFBBBRLL",
    "BBBBFFBLRL",
    "FBBFBBFRLL",
    "BFFBBBBRLL",
    "BFBBBFBRRL",
    "BBFBFBFLLR",
    "FFFBBBBLLR",
    "BFFBBFFLRR",
    "BBBFBBBLRL",
    "FBBFBFFRRL",
    "BBFBFFFRRL",
    "BBFBFFBLRR",
    "BBBFBBFRLR",
    "FBBBFBFRRR",
    "BBFBFBFLRL",
    "FBBFBBFLRL",
    "FFBFFFFLRR",
    "BFBBFBBRRL",
    "FBBBBFFRRL",
    "FBFBFFBRRR",
    "BBBFFBFLLL",
    "FFFBFFFLRL",
    "FBFBBBFRRR",
    "BBBFBFFRRL",
    "BFBFFFBLRL",
    "BBBFBFFLRR",
    "BFFFBFFLLL",
    "FFBFBBFLLR",
    "FFBFBBFRLL",
    "FBFBBBFLRL",
    "BFFBBBBRRL",
    "FBBBFBFRRL",
    "FFBBBFBLLL",
    "BFBBBFFLRL",
    "BBBBBFFLLR",
    "FBFBFFFRRL",
    "BFFBFBBLRR",
    "BBFFFFBLRR",
    "FBFFBFBLRR",
    "FBFFBBFRLR",
    "FFBBFFBLRL",
    "FFFFFBBLRR",
    "BBBBBFFLRR",
    "BFBBBBFLLL",
    "FBBFBFFRRR",
    "FFFFFBBLLR",
    "FFBFFBFLLL",
    "FFBFBBBLRR",
    "FFBBFBFRLR",
    "BFBBBFFRRR",
    "FBFFBFBRLR",
    "BBBFBBFLLR",
    "BFBBFBFLRR",
    "FBBBFFBLRL",
    "BFBBBBBRLR",
    "FBBFBBFLLR",
    "BFBBBFFRLR",
    "FBBBBBFLRL",
    "BFBBBBBRRR",
    "BFFBBBBRRR",
    "BBFBFBFLRR",
    "BFFBBBBLLL",
    "BBFFFBFLRL",
    "BFBBFBFLLL",
    "FBFFFFBRRL",
    "FFBBBBFRRR",
    "FFBFBBBRLR",
    "BBFBFBFLLL",
    "FBFFBFBRRR",
    "FFFBBBFLLR",
    "FFFBFBFLRL",
    "BFBFBBBLRL",
    "FBBFFBBLLL",
    "BBBFBFBRRL",
    "FBFFFBBRRR",
    "BFFFBFBLLL",
    "FFFFBFBLLL",
    "FFFBBFBRLL",
    "FBBFFFBRRL",
    "FFBBFBFLLL",
    "FFBBFFBRLL",
    "FBFBFBFLLR",
    "BBFFFFBLRL",
    "BFBFBBFRRL",
    "FFFBFBBRLL",
    "FBBFFBBRLL",
    "BBFBFBBLLR",
    "BFFFBFFRLL",
    "BFBFBFFLRR",
    "FBFFFFBLLR",
    "FFFBBFBRRL",
    "FFFBBBBLRL",
    "FFBBFFBLRR",
    "BFFFBBFLLL",
    "FFFBFFFLLL",
    "FBFBFBFRRR",
    "BFBBBFBLLR",
    "BFFBFFFRRL",
    "FFFFBBFLRR",
    "FBFBFBFRRL",
    "BFBBFBBRRR",
    "BFBFFBBLRL",
    "FBFBBFBRLL",
    "FBBBBFFLRL",
    "FFBFBFFLRL",
    "FBBFBBBRRR",
    "FBFBFBFRLR",
    "FFBFFFFLRL",
    "BBFBFBBRLR",
    "BFBFFBBRLL",
    "BBFFBFBRRR",
    "BFBBBBBRRL",
    "BBFBBBFLLR",
    "BBFFBBBRLR",
    "BBFBFFFLLR",
    "FFFFBBFLLL",
    "FBBFFFFRRR",
    "BBFBFFBRLL",
    "FFBBFBBLLL",
    "BFBBFFFRRR",
    "BFBBFFFRLL",
    "BFFBBFFRRL",
    "BBFBBBFRRR",
    "BFFFBFBRLL",
    "BFFFBBBRRL",
    "FBFBBFFLLR",
    "FBFFBBFRLL",
    "BBFBBFBLRR",
    "BBBFFFFLLR",
    "FBBFBBBLLL",
    "FBFFBBFLLL",
    "BFFBFBBLRL",
    "BBFFFFFRRL",
    "FFBBBBBRLL",
    "FBFFBFFLLL",
    "FFFFFBFRRL",
    "BBBBFFBRRL",
    "FBBFBFBRLR",
    "BBFBBFBRLR",
    "BFFBBFBLRR",
    "BFFFFBBLLL",
    "BBBBFBBRRR",
    "BBBFFFBLLR",
    "FFBFFFFLLL",
    "FBBFFBFLLR",
    "BBFFFFFLRL",
    "FFFFBBBLRR",
    "FBBBBFFLLL",
    "FFBBFFBLLL",
    "BBFBFFBRRR",
    "FBFBFBFLRL",
    "FFFBBBFLRR",
    "BFBBBFBLRR",
    "FBBBBBFLLR",
    "BBFFBBBLRL",
    "FFBFFBFLLR",
    "FFFBBBFRLL",
    "FBFFFBBRLL",
    "BFFBFBFLLR",
    "FFBBBFBRLR",
    "BBFFFBBLRR",
    "BFFFBBFLRL",
    "FFFBBFFLRR",
    "BBBFBBBLLL",
    "BBFBFFFRLL",
    "FFFBBFFRRL",
    "BFBBFFFLRR",
    "BBFFFFBRRR",
    "BBFFFFFLLR",
    "BBFBBBBLRL",
    "FFBFBBBLRL",
    "BBFFFFFRRR",
    "FBFBFFBLLL",
    "BFFBBBFLRR",
    "FFFFFBBRRL",
    "BFFFFFBRRL",
    "BBBFBFFRLL",
    "FBFFBBFLLR",
    "BBBFFBFRRR",
    "BBFBFFFLRR",
    "BBFFBBFLRR",
    "BFBFFBFRRL",
    "FBBBFBBRRR",
    "BBFFBFFLRR",
    "BBFBFFFRLR",
    "FBBBBBFRRL",
    "BFFFBBFLLR",
    "BBFBBFFLLR",
    "FBFFFFFLLR",
    "FFFBBFFRLL",
    "BBFBBFFRLL",
    "FFFFBBBLLL",
    "BFBFFBBRLR",
    "FBBFBBBLLR",
    "BFFBBBFLLR",
    "BFFFFFFLRL",
    "BFFBBBFLLL",
    "BFBFFBFLLL",
    "BBFBFFBLLL",
    "FFBBBBFRLL",
    "FBFFBFFLRR",
    "BBBFFBBRRL",
    "BFFBBFFRRR",
    "BBBBFFFLLR",
    "BFBBFFBRRR",
    "FBFFFBFRLL",
    "FFBBBFFRLL",
    "FBBBBFBLRR",
    "FFFBBFBLRR",
    "FFBBFFFLRR",
    "BBFBBBFLRR",
    "FBFBFFBRLR",
    "FBBFFBBLLR",
    "BBFFBBBLRR",
    "BBFBFFBLLR",
    "FBBFFFBLRL",
    "BFBFBFFLRL",
    "FFFBFFFRLR",
    "FBFBFFFLRL",
    "BBBFFBFRLR",
    "BBBFBBFLLL",
    "FBFBFBBLLR",
    "BFBFBFFLLL",
    "FFBFFFBRRR",
    "BFBFBFFRLR",
    "FFFBBBBLRR",
    "BBFBBFFLRL",
    "FFBFFFFRRL",
    "BFBFFBFLLR",
    "FFBBBBFLLR",
    "FBFBBBBRRR",
    "FFBFFBFLRL",
    "FBBBBBBRLL",
    "BBFBFBBLLL",
    "FBBFFBBRRL",
    "FBBBBBBRRL"
]


def main(input):
    plane = []
    for i in range(0, 127):
        plane.append(["O", "O", "O", "O", "O", "O", "O", "O"])
    biggest = 0
    for i in input:
        row = [0, 127]
        for j in i[:-3]:
            if j == "F":
                row[1] = row[1]-math.ceil((row[1]-row[0])/2)
            else:
                row[0] = row[0]+math.ceil((row[1]-row[0])/2)

        col = [0, 8]
        for j in i[-3:]:
            if j == "L":
                col[1] = col[1]-math.ceil((col[1]-col[0])/2)
            else:
                col[0] = col[0]+math.ceil((col[1]-col[0])/2)
        biggest = max(biggest, row[0]*8+col[0])
        plane[row[0]][col[0]] = "X"

    return plane


tmp = main(input)

for i in range(len(tmp)):
    if "O" in tmp[i] and 5 < i < 120:
        print((i*8)+7)
