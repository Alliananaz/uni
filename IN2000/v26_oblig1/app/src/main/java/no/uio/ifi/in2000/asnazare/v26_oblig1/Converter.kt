package no.uio.ifi.in2000.asnazare.v26_oblig1

import kotlin.math.roundToInt

fun converter (verdi: Int, enhet: ConverterUnits ): Int {
    return when (enhet){
        ConverterUnits.OUNCE -> (verdi * 0.02957).roundToInt()
        ConverterUnits.CUP -> (verdi * 0.23659).roundToInt()
        ConverterUnits.GALLON -> (verdi * 3.78541).roundToInt()
        ConverterUnits.HOGSHEAD -> (verdi * 238.481).roundToInt()
        else -> 0
    }
}