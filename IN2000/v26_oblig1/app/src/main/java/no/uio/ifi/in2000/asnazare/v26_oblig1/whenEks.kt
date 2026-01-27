package no.uio.ifi.in2000.asnazare.v26_oblig1

enum class Farge {
    ROD, BLAA
}

// Hva mangler her? (Dersom inputen ikke er "rød" eller "blå")
fun velgFarge(input: String) {
    when (input) {
        "rød" -> println("Du valgte ${Farge.ROD}")
        "blå" -> println("Du valgte ${Farge.BLAA}")
        else -> println("Du valgte feil farge oopsie")
    }
}

fun main (){
    velgFarge("gronn")
}



