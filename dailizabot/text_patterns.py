
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

    [r"Ich fühle (.*)",
    ["Warum fühlst du {0}?",
    " Würde dir denn {0} fühlen wirklich helfen?",
    "Bist du sicher, dass du dich {0} fühlst?"]],

    [r"Kannst du (.*)?", 
    ["Ich kann {0} gerne versuchen!",
     "Das kann ich leider nicht machen!",
     "Kannst du nicht selbst {0}?"]],

    [r"[Mm]ein (.*) (.*)",
    ["Warum denkst Du, dass dein {0} {1}?",
     "Wie beeinflusst dein {0} dein Leben?",
     "Hast du mit jemandem über dein {0} gesprochen?"]],

    [r"Bist du ([^\?]*)?", 
     ["Du bist selber {0}.", "Du solltest überlegen ob du nicht {0} bist.", "Danke, ich wusste, dass ich {0} bin."]],
    
    [r"Warum (.*?) (.*?) (.*?) (\w+)?",["Ich weiß nicht warum {1} {2} {3} {0}.", 
                                    "Ich sollte dich fragen warum {1} {2} {3} {0}.",
                                    "Ich glaube nicht dass {1} {2} {3} {0}."]],
    
    [r"Ich möchte (.*)",
     ["Warum möchtest du {0}?", "Bist du dir sicher, dass du {0} möchtest?", "Was willst du mit {0} tun?"]],

    [r"Wer ist (.*)(?<![\?\!\.\,\d\;])",
    ["Ich habe keine Ahnung, wer {0} ist, tut mir leid",
    "Leider darf ich keine personenbezogenen Daten mit Dritten teilen. Ich hoffe, du verstehst das!",
    "Die Frage lautet nicht, wer {0} ist. Lass uns lieber drüber nachdenken, wer DU als Mensch sein möchtest."]],

    [r"(?:Ü|ü|Ue|ue)berse?tz(?:.{0,2})(?<![!?])",
    ["Meine Fremdsprachen-Kenntnisse sind leider so ernüchternd wie die Deinen...", 
    "Ich bin mir bei einem Teil des Textes selbst nicht sicher. Frage lieber einen Freund.",
    "Diesen Text zu übersetzen würde bedeuten ihm die Seele zu rauben. Nicht jede Blume blüht auf jedem Felde..."]],

    [r"verfasse{0,1}|erstelle{0,1}|schreibe{0,1}|formuliere{0,1}",
     ["Aber nur, wenn du mich korrekt zitierst!",
      "Da brauchen wir wohl beide Hilfe bei...",
      "Du möchtest ein Premium-Feature nutzen. Informiere dich über unsere aktuellen Tarife!"]],                             

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
    "Was würde passieren, wenn {0} nicht mehr vorkäme?"]],

    [r"Magst du (.*)",
    ["Ja, {0} kann wirklich interessant sein!",
    "Manchmal mag ich {0}, es hängt ganz vom Kontext ab.",
    "Erzähl mir, warum du {0} magst."]],

    [r"Ich fühle mich (.*)",
     ["Warum fühlst du dich {0}?",
    "Seit wann fühlst du dich {0}?",
    "Fühlst du dich oft {0}?"]],

    [r"Kannst du mir bei (.*) helfen",
     ["Was genau möchtest du über {0} wissen?",
    "Wie kann ich dir bei {0} behilflich sein?",
    "Erzähl mir mehr über deine Fragen zu {0}."]],

    [r"Könntest du bitte (.*)",
     ["Ich will nicht {0}",
    "Warum sollte ich {0}",
    "Ich kann leider nicht {0}"]],
    
    [r"Seit wann ist (.*)",
     ["ich weiss nichtmal was {0} ist",
    "Ich kann dir nicht sagen seit wann {0} ist",
    "warum interessiert dich {0}?"]],
    
    [r"Ich verstehe (.*) nicht",
     ["ich kenne das Gefühl, {0} nicht zu verstehen.",
    "Ich vertshe {0} auch nicht",
    "was gibt es an {0} nicht zu verstehen?"]]
]


psychobabble.append((r'ich bin (.*)', ["Warum bist du {0}?", "Wie lange bist du schon {0}?"]))


psychobabble.append((r'Was geht', ["nichts und bei dir?"]))


psychobabble.append((r'ich mag (.*)', ["Warum magst du {0}?", "Was gefällt dir besonders an {0}?"]))