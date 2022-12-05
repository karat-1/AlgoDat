"""
Algorithmen und Datenstrukturen
ESA1 Aufgabe 1 h)

Ja, es gibt bessere Lösungen aber nicht ohne einen gewissen Preis (mehr Speicherplatz), oder keinen Leistungszuwachs in Worst-Cases.
Die Funktion largest_distance_optimized() bricht aus der Schleife heraus sobald largest
größer ist als der absolute Wert von i - die Länge des Arrays. Wenn wir uns am einen Punkt befinden
wo es keine größere Distanz mehr geben errechnet werden kann muss die Schleife nicht weiter fortgeführt werden. Außerhalb der beiden
Worst-Cases (ein Array ohne Duplikate und ein Array aus ausschließlich Duplikaten) wird Zeit gewonnen.
Da wir hier aber ausschließlich von Worst-Cases ausgehen bleibt die Komplexitätsklasse bei Θ(n^2).

Die Implementation von largest_distance_dict() nutzt eine Hashmap bzw. Dictionary als Datenstruktur welches jede Zahl im
Eingabearray als Schlüssel nutzt und speichert unter jedem Schlüssel eine Liste der Indexe wo sich die Zahlen
im Array befinden. Hier müssen wir nur maximal 3x durch das Eingabearray iterieren. Einmal um alle Werte in das
Dictionary zu schreiben, einmal um durch das Dictionary zu iterieren, und einmal durch die jeweiligen Listen die unter jedem
Schlüssel im Dictionary abgelegt sind. Die Listen die unter den Schlüssen abgelegt sind, sind jedoch alle zusammen nur so lang wie das Eingabearray.
Dementsprechend ist die Zeitkomplexität Θ(n).
"""


def largest_distance(n):
    largest = 0
    z = n[0]
    counter = 0
    inner_counter = 0
    for i, element_one in enumerate(n):
        for j, element_two in enumerate(n):
            counter += 1
            if n[i] == n[j]:
                if (j - i) > largest:
                    inner_counter += 1
                    largest = (j - i)
                    z = n[j]
    print("Schrittzaehler: " + str(counter))
    print("Innerer Schrittzaehler: " + str(inner_counter))
    return z


def largest_distance_optimized(n):
    largest = 0
    z = n[0]
    counter = 0
    for i, element_one in enumerate(n):
        for j, element_two in enumerate(n):
            counter += 1
            if n[i] == n[j]:
                if (j - i) > largest:
                    largest = (j - i)
                    z = n[j]
        # Exitkondition für die Schleife
        if largest >= abs(i - len(n)):
            break
    print("Schrittzaehler: " + str(counter))
    return z


def largest_distance_dict(n: list):
    number_dict = {}
    largest = 0
    z = n[0]
    counter = 0
    for i, element in enumerate(n):
        counter += 1
        if element in number_dict:
            number_dict[element].append(i)
        else:
            number_dict[element] = [i]

    for key in number_dict:
        counter += 1
        indices = number_dict[key]
        for i, index in enumerate(indices):
            if i < len(indices) - 1:
                counter += 1
                if indices[i + 1] - i > largest:
                    largest = indices[i + 1] - i
                    z = key
    print("Schrittzaehler: " + str(counter))
    return z


input_array = [3, 5, 2, 3, 2, 0, 2, 3, 1, 5]
input_array_worst_case = [1, 1, 1, 1, 1, 1, 1, 1]
print("Ausgabewert: " + str((largest_distance_dict(input_array_worst_case))))
