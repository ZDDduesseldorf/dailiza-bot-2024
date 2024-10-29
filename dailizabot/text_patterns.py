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

]
