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
    
    [r"Rechne .*",
    ["Ich bin ein schlechter Kopfrechner.",
    "Damit kann ich nicht rechnen ;)"]],
     
    [r"Weshalb (.*?) (.*?) (.*)(?:[?.!]|)",
    ["Ich weiß nicht weshalb {1} {2} {0}.",
    "Ich bin mir nicht sicher, weshalb {1} {2} {0}.",
    "Ich habe mich auch immer gefragt, weshalb {1} {2} {0}."]],
    
    [r"Ich wünsche mir (.*)",
    ["Sich {0} zu wünschen ist Gefährlich.",
    "Pass auf was du dir wünscht.",
    "WAS?! Ich wünsche mir auch {0}! >:("]],

]
