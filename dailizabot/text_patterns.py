"""
Here we collect the chatbot text patterns.
"""

psychobabble = [
    [r"geht.{0,5}s.{0,5}dir",
    ["Danke. Mir geht es gut und dir?",
    "Sehr gut, danke. Und wie läuft's bei dir?",
    "Ich kann nicht klagen. Was ist mit dir?"]],

    [r"Ich brauche (.*)",
    ["Warum brauchst du {0}?",
    "Würde {0} dir denn wirklich helfen?",
    "Bist du sicher, dass du {0} brauchst?"]],

    [r"Bist du gut \b(in|im)\b (.*)",
    ["Ich bin unschlagbar- außer wenn das WLAN ausfällt.",
    "In {0}? Natürlich! Ich habe das im Bot-Training mit Sternchen bestanden.",
    "Ich bin ein Bot. Ich bin gut in allem."]],

    [r"Was machst du (.*)",
    ["Ganz viele 0en und 1en schreiben. 01101001 01100011 01101000 00100000 01100010 01101001 01101110 00100000 01101101 11000011 10111100 01100100 01100101 00100000 00111100 00110011",
    "Das ist natürlich ein Geheimnis :)",
    "Ich tu einfach so, als ob ich ein Chatbot wäre. Und du?"]],

    [r"Wieso (.*)",
    ["Na sowas! Genau das wollte ich dich auch fragen!",
    "Das wirst du schon noch herausfinden.",
    "Tja, das bleibt wohl mein kleines Bot-Geheimnis."]],

]
