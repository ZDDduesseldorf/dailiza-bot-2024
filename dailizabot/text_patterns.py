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

    [r"Ich f(ü|ue|u)hle mich (.*)",
    ["Warum fühlst du dich {1}?",
    "Was denkst du, hat dazu geführt, dass du dich {1} fühlst?",
    "Wie lange fühlst du dich schon {1}?"]],

    [r"Ich kann nicht (.*)",
    ["Warum denkst du, dass du {0} nicht kannst?",
    "Hast du schon mal darüber nachgedacht, warum du {0} nicht kannst?",
    "Was hält dich davon ab, {0} zu können?"]],

    [r"Warum passiert mir immer,? (.*)",
    ["Warum glaubst du, dass dir immer {0} passiert?",
    "Meinst du, dass es einen Grund gibt, warum dir immer {0} passiert?",
    "Was würde passieren, wenn {0} nicht mehr vorkäme?"]]
]
